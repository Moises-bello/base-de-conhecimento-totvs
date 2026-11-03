---
content_hash: d205c328a857ab3805317adeed6351844a337d1f05fa1de38be99882091b7892
fetched_at: '2026-06-29T00:11:22.086900+00:00'
page_id: '698289155'
product: rm
source: tdn-rm
title: Configurar Parâmetros no RM.exe para Abrir Action
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=698289155
version: 4
---

# Índice

---

* [Índice](https://tdn.totvs.com/pages/viewpage.action?pageId=403746913#Loginap%C3%B3saltera%C3%A7%C3%A3odecredenciasdoBancodedados-%C3%8Dndice)
* [Objetivo](https://tdn.totvs.com/pages/viewpage.action?pageId=403746913#Loginap%C3%B3saltera%C3%A7%C3%A3odecredenciasdoBancodedados-Objetivo)
* [Configuração do Atalho](https://tdn.totvs.com/pages/editpage.action?pageId=698289155)

# Objetivo

---

        Disponibilizar ao usuário funcionalidade para adicionar parâmetros no RM.exe (Atalho) que permita abrir uma action passando parâmetro ou não.

# Configuração do Atalho

---

Atenção

Funcionalidade disponíveis a partir dos patches das versões **12.1.33.288**, **12.1.34.186**  e **12.1.2205.126**.

Para usar essa funcionalidade basta criar um atalho do RM.exe e adicionar os parâmetros seguinte a seguinte estrutura:

* diretório onde está o RM.exe runact=Nome da action?PK=ID alias=ALIAS user=USUARIO password=SENHA

***Exemplo***:

Para abrir o RM com a tela de coligada aberta no registro 1:

*C:\RM\Legado\12.1.33\Bin\RM.exe runact=GlbColigadaAction?PK:1 alias=CorporeRM user=mestre password=totvs*

Para abrir o RM com a tela de coligada em modo de inserção de uma nova coligada

*C:\RM\Legado\12.1.33\Bin\RM.exe runact=GlbColigadaAction?PK:null alias=CorporeRM user=mestre password=totv*s
