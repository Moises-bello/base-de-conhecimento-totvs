---
article_id: 360020492412
category: RH - Error.log
content_hash: 2ef50e084c2c3097aa0ffc15dcf9d96870d4bb289593d9ac736bc48108e7785c
fetched_at: '2026-06-28T22:44:49.502746+00:00'
product: protheus
section_id: 32419193161751
source: central-protheus
title: RH - Linha Protheus - PON -  Ao tentar acessar a rotina de Integrados e realizar
  qualquer operação é apresentado o error log array out of bounds ( 0 of 29 ) on F_ALT_H(PONA040.PRX)
type: support-article
updated_at: '2025-06-13T19:42:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020492412-RH-Linha-Protheus-PON-Ao-tentar-acessar-a-rotina-de-Integrados-e-realizar-qualquer-opera%C3%A7%C3%A3o-%C3%A9-apresentado-o-error-log-array-out-of-bounds-0-of-29-on-F-ALT-H-PONA040-PRX
---

**Ocorrência**Ao tentar acessar a rotina de Integrados e realizar qualquer operação é apresentado o *error log* array out of bounds ( 0 of 29 ) on F\_ALT\_H(PONA040.PRX)  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**   
Esse incidente ocorre devido o campo **P8\_DATAAPO** não estar configurado como "usado" no Dicionário de Dados.  
  
**Solução**  
Para solucionar ocorrência, realizar os seguintes passos:  
1. Acessar o Configurador;  
2. Base de Dados;  
3. Dicionário;  
4. Base de Dados;  
5. Clicar em Dicionário de Dados e pesquisar a tabela SP8**;**  
6. Clicar em editar, depois campos;  
7. Selecionar o campo P8\_DATAAPO e clicar em editar;  
8. Na aba Uso deixar a opção Usado selecionado;  
9. Salvar e Atualizar.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062920474/mceclip0.png)
