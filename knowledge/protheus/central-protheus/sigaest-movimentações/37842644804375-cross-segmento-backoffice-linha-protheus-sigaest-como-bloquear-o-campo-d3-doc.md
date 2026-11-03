---
article_id: 37842644804375
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 4f4a1ab041d2b1ee10dc2915464ffdf9e97eadca144bef6bb77a985fe0372179
fetched_at: '2026-06-28T22:38:54.360316+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como bloquear o campo
  D3_DOC?
type: support-article
updated_at: '2026-01-21T21:34:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37842644804375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-bloquear-o-campo-D3-DOC
---

Para bloquear o campo D3\_DOC no cabeçalho das rotinas Movimentação Múltiplas, Transferência entre Armazém e Baixa da Pré-Requisição no TOTVS Protheus, acesse o Configurador em Base de Dados - Dicionário, selecione a tabela SD3 no campo D3\_DOC e defina a propriedade como "visualizar". Também é possível compilar os pontos de entrada das rotinas MATA241, MATA261 e MATA185 para controlar a digitação dos documentos pelos usuários.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37842644788759) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como bloquear o campo D3\_DOC para não permitir a digitação do número de documento  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Para bloquear o campo D3\_DOC no cabeçalho das rotina Movimentação Múltiplas, Transferência entre Armazém e Baixa da Pré-Requisição, realizar o seguinte procedimento.

* Acessar o Configurador na opção Base de Dados - Dicionário - Base de Dados
* Seleciona a tabela SD3, posicionado no campo D3\_DOC
* No campo D3\_DOC seleciona a propriedade do campo como visualizar, dessa forma ira bloquear o campo de documento.![](https://centraldeatendimento.totvs.com/hc/article_attachments/37842644790039)

Para essa necessidade também é possível compilar os pontos de entrada abaixo, para indicar se o usuário pode ou não digitar os documentos:  
   
**MATA241**: [MTA241DOC](https://%C2%A0https://tdn.totvs.com/x/duRc%C2%A0)  
**MATA261** e **MATA185**: [MTA261DOC](https://tdn.totvs.com/x/heRc)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
