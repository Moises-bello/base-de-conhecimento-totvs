---
content_hash: 261a5e9c24b9e9770efc419b72cfeed44d647ca72be7a4a0badd025ce8ceae80
fetched_at: '2026-06-29T00:09:30.274693+00:00'
page_id: '425458407'
product: rm
source: tdn-rm
title: Sincronizar Usuários Corpore Usuário ECM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458407
version: 2
---

**Sincronizar Usuários Corpore Usuário ECM**

---

O processo "Sincronizar Usuários Corpore Usuário ECM" criará/atualizará como colaborador no TOTVS ECM (disponibilizando-o para uso/acesso às solicitações do workFlow) os usuários da linha RM atualmente cadastrados no módulo de cadastro de usuários. Os campos dos usuários a serem transpostos neste processo são: código do usuário, nome, e-mail e código da companhia (do ECM) setado no registro de tipo de atendimento selecionado.  
   
A senha não irá trafegar neste ponto, pois a mesma está criptografada e não há retorno. Não foi disponibilizado rotina para descriptografar porque não é aconselhável publicar o método de criptografia e sincronizar. O uso do atributo pode ser alterado tanto no ECM quanto no TOTVS Aprovações e Atendimento e isto impactaria na validação ao acesso aos WebServices.  
   
Como evolução da integração, será estudado a possibilidade de uso da autenticação integrada  através do Active Directory.  
   
Procedimentos:

* Acesse  o cadastro de Tipos de atendimentos .
* Selecione o registro, que está integrado com o TOTVS ECM, que se deseja sincronizar os usuários;
* Execute o processo "Sincronizar Usuários do Corpore com Usuário ECM".
