from operator import index
from flask import Blueprint, jsonify
from app.models.grupo_dois_model import GrupoDoisModel

bp_grupos = Blueprint("bp_grupos", __name__)


@bp_grupos.get("/grupos")
def get_all_couples():
    list = GrupoDoisModel.query.all()

    return jsonify([
            {"nome": person.nome,
            "conjuge": {
                "nome": person.conjuge.nome
            }} for person in list
        ]), 200

@bp_grupos.get("/grupos/por_limite/<int:limite>")
def get_couples_by_limit(limite):
    list = GrupoDoisModel.query.all()
    limited_list = list[0:limite]

    return jsonify([
            {"nome": person.nome,
            "conjuge": {
                "nome": person.conjuge.nome
            }} for person in limited_list
        ]), 200

@bp_grupos.get("/grupos/inicia_pelo_caractere/<caractere>")
def get_couples_by_initial(caractere):
    list = GrupoDoisModel.query.filter(GrupoDoisModel.nome.startswith(caractere.title())).all()
    
    return jsonify([
            {"nome": person.nome,
            "conjuge": {
                "nome": person.conjuge.nome
            }} for person in list
        ]), 200

@bp_grupos.get("/grupos/termina_pelo_caractere/<caractere>")
def get_couples_by_last_character(caractere):
    list = GrupoDoisModel.query.filter(GrupoDoisModel.nome.endswith(caractere.lower())).all()
    
    return jsonify([
            {"nome": person.nome,
            "conjuge": {
                "nome": person.conjuge.nome
            }} for person in list
        ]), 200

@bp_grupos.get("/grupos/por_idade/<int:idade>")
def get_couples_by_age(idade):
    list = GrupoDoisModel.query.filter(GrupoDoisModel.idade == idade).all()
    
    return jsonify([
            {"nome": person.nome,
            "conjuge": {
                "nome": person.conjuge.nome
            }} for person in list
        ]), 200

@bp_grupos.get("/grupos/pelo_id/<int:id>")
def get_couples_by_id(id):
    person = GrupoDoisModel.query.get(id)
    
    return {"nome": person.nome,
            "conjuge": {
                "nome": person.conjuge.nome
            }}, 200