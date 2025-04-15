from models import session, Usuario
import streamlit_authenticator as stauth

senha_criptografada = stauth.Hasher(["senha123"]).generate()[0]
usuario = Usuario(nome="Luan", senha=senha_criptografada, email="luanadm@gmail.com", admin=True)
session.add(usuario)
session.commit()