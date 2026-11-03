---
content_hash: 36096abe61425cab0b74b4d646ccd4bf52f1a6af666614f88d03720c77609cb1
fetched_at: '2026-06-29T00:05:55.726686+00:00'
page_id: '146179365'
product: rm
source: tdn-rm
title: Logon Unificado
type: documentation
url: https://tdn.totvs.com/display/LRM/Logon+Unificado
version: 19
---

# Índice:

---

.\*ndice:

Vulnerabilidades de segurança conhecidas

Este formato de login não é recomendado em casos de *ambientes cloud ou redes abertas* pois apresenta falhas de seguranças inerentes à arquitetura da solução.  
Reforçamos nesses casos que o parâmetro seja desligado com urgência.

Para continuar com a funcionalidade de SSO (Single Sign On) no sistema, indicamos fazê-lo atráves de protocolos seguros que já são suportados pelo RM, listados a seguir com os respectivos links:

# Objetivo

---

       O objetivo deste documento é demonstrar como utilizar o Logon Unificado no RM. Disponibilizamos a seguir o passo a passo da configuração e uma vídeo aula com a explicação.

       Quando o RM está configurado para utilizar o logon unificado, ao abrir o RM.exe o sistema entrará, automaticamente com o usuário de rede, sem o usuário precisar informar sua senha. Essa configuração pode ser feita de duas formas: Utilizando usuário do RM ou utilizando usuário da rede. Veja a seguir como funciona.

# Logon Unificado

---

****Configurando o Logon Unificado - Passo a Passo:****

* Para ativar o Logon Unificado, acesse o Menu Ambientes > Parâmetros > Parâmetros Globais:

* Acesse a aba Gerais:
* Marque a configuração 'Ativar Logon Unificado'.  
    
  **Observação:** Serão habilitados os parâmetros 'Nome do Usuário' quando pelo menos 1 usuário da base tiver a aba 'Rede' preenchida no cadastro de Usuários.   
  Se os dados da aba Rede não existirem na base, o Logon Unificado será ativado por padrão como 'Utilizar usuário do RM'.

# Logon Unificado utilizando usuário do RM

---

**Utilizar usuário do RM:**

O código do usuário precisa ser criado com o mesmo usuário da rede.  
O login será feito com o usuário que é o mesmo da rede e a senha do RM.

Exemplo: Foi criado o usuário "stella.vilaca" e a aba rede está em branco. Depois foi configurado o Logon Unificado utilizando o usuário do RM:

O usuário logado no computador também é "stella.vilaca". Ao abrir o RM.exe ele entrará com o usuário 'stella.vilaca' automaticamente. Sem precisar informar a senha.

# Logon Unificado utilizando usuário da Rede

---

**Utilizar usuário da Rede:**

O sistema fará login automaticamente com o usuário de rede.  
Para isso, deve ser preenchida a aba 'Rede do cadastro de usuário'.

Exemplo: Foi criado o usuário "mestre" e a aba rede está foi preenchida. Depois foi configurado o Logon Unificado utilizando o usuário de rede.

O usuário logado no computador também é "stella.vilaca". Ao abrir o RM.exe ele entrará com o usuário 'Mestre' automaticamente. Sem precisar informar a senha.

Observação:

O código do usuário informado no cadastro do usuário no RM  deve ser idêntico ao cadastrado na rede. A senha cadastrada não precisa ser a mesma da rede.

**Veja também um exemplo do processo em vídeo:**

700393

Leia sobre .

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX ou 12.01.XX

false

**Processo:** Logon Unificado

false

**Subprocesso:** Parametrização do RM para Logon Unificado

falsefalse

**Status:** Finalizado

false

**Data:** 03/04/2018

false

**Autores:**
