---
content_hash: 2fdedebd7d21791a7d6f3e7940cfbdde0027f6ba4a0c611ba4dfcbb30b8e0d0e
fetched_at: '2026-06-28T21:35:26.680775+00:00'
page_id: '392500315'
product: fluig
source: tdn-fluig
title: APIs LMS
type: documentation
url: https://tdn.totvs.com/display/fluig/APIs+LMS
version: 25
---

Importante!

A partir de **Abril de 2025**, o [suporte](https://totvscst.zendesk.com/hc/pt-br/#home) ofertado ao LMS será descontinuado. Não havendo mais evoluções após este período. O LMS não estará mais disponível para acesso nos ambientes a partir da **próxima release** do TOTVS Fluig Plataforma prevista para o primeiro semestre de 2025.

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é disponibilizar as APIs específicas do LMS da plataforma TOTVS Fluig para consulta.

Atenção!

Salientamos que essas APIs são válidas para uso, porém, estão em **processo de** **depreciação**.

# Visualizar as APIs

Para visualizar as APIs atuais do LMS efetue os seguintes passos:

0.5falsesamplesfadetrue1Passo 1

O LMS possui duas versões de APIs e é possível visualizar a documentação de cada uma das versões na própria plataforma, acessando o endereço /lms/swagger/{versão}/swagger.json:

* versão 1 → {meu\_fluig}/lms/swagger/v1/swagger.json;

* versão 2 → {meu\_fluig}/lms/swagger/v2/swagger.json.

Exemplo:  
https://minhaempresa.fluig.com/lms/swagger/v2/swagger.json

2Passo 2

Ao acessar os endereços citados no passo anterior, será exibido na página um JSON da API no formato Swagger.

* Copie o JSON para colar em um leitor de documentação Swagger *on-lin*e para uma melhor visualização da documentação da API.
* Acesse o endereço [https://editor.swagger.io](https://editor.swagger.io/) e cole o JSON no editor para visualizar a documentação. Após colar o JSON no editor, pode ser que seja apresentado um *log* com erros de semântica da documentação. Nesse caso, basta clicar em "Hide" para esconde-los e visualizar a documentação das APIs.

**À direita é exibido um modelo navegável da documentação onde é possível consultar os caminhos e modelos utilizados da API.**

* Caso ainda não visualize, pode ser necessário remover as linhas iniciais que contenham comentários. Exemplo:

jsLinhas a serem removidas
