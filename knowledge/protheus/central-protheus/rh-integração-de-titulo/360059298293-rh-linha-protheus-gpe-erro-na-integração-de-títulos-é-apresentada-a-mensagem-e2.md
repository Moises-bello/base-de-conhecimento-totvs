---
article_id: 360059298293
category: RH - Integração de Titulo
content_hash: 43025c4134952584e3cdd97cb38c3f1ef75ca8e8ac9688c36fcdc5e8baa779d7
fetched_at: '2026-06-28T22:43:37.186962+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro na integração de títulos é apresentada a
  mensagem: E2_TIPO <-- Inválido'
type: support-article
updated_at: '2025-08-12T12:28:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059298293-RH-Linha-Protheus-GPE-Erro-na-integra%C3%A7%C3%A3o-de-t%C3%ADtulos-%C3%A9-apresentada-a-mensagem-E2-TIPO-Inv%C3%A1lido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34118901131799) Tempo aproximado para leitura: **00:01:00 min****

**Ocorrência**Na integração de títulos é apresentada a mensagem: E2\_TIPO <-- Inválido  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, pois na rotina **Tabelas Genéricas**, a chave do **Tipo de Titulo** foi parametrizado com tamanho superior ao aceito pelo campo **Tipo** (**E2\_TIPO**) do módulo **Financeiro - SIGAFIN** que por padrão possui um tamanho de 3 posições.  
  
**Solução**Erro apresentado:  **![e2_tipo_invalido.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360099685273)**

Para solucionar essa ocorrência: 

**Acessar:** SIGACFG ->Base de Dados ->Dicionário ->Base de Dados  ->Tabelas Dinâmicas, efetuar a busca pela Tabela 05 - Tipos de Títulos

![tabela_05.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360099686053)

No print acima é possível verificar que a chave do tipo de título INSS foi cadastrado com 4 posições, portanto deve ser ajustado para apenas 3 posições conforme o padrão.

Após este processo o título que foi invalidado deve ser gerado novamente e posteriormente integrado.

**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
[RH - Linha Protheus - GPE - Como cadastrar "tipo de título" na rotina de Definição de Títulos (GPEM640)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038134413-MP-GPE-Como-cadastrar-tipo-de-t%C3%ADtulo-na-rotina-de-Defini%C3%A7%C3%A3o-de-T%C3%ADtulos-GPEM640-)
