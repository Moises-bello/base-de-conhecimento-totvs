---
article_id: 360024630454
category: RH - CNAB
content_hash: c20dae78e42882ee29e4612e0aceefbdf2ea4d2b257727bff78027289486eead
fetched_at: '2026-06-28T22:43:39.304003+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Parâmetro Processar Banco na geração do Arquivo
  CNAB (GPEM080)
type: support-article
updated_at: '2025-06-17T19:18:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024630454-RH-Linha-Protheus-GPE-Par%C3%A2metro-Processar-Banco-na-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32879266719511)**Tempo aproximado para leitura:**01:00:00 min**

**Dúvida**  
Como utilizar o parâmetro **Processar Banco** na Geração do arquivo CNAB?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para utilizar o parâmetro **Processar Banco?** na rotina **GPEM080** , é necessário preencher a **tabela S052 - Parâmetros** **para CNAB/SISPAG** na manutenção de tabelas (Atualizações-> Definições de Cálculo-> Manutenção de Tabelas).   
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038043914)

Esta tabela permite incluir e definir a estrutura de novas tabelas, chamadas de **tabelas auxiliares**, pois ampliam os controles cadastrais e de cálculos oferecidos pelo Sistema.

As tabelas podem ser diferenciadas entre filiais se houver necessidade, caso contrário deverá manter o campo **Filial** em branco para que a tabela seja comum a todas as filiais.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038888393)

Os valores serão gerados para as formas de pagamento crédito em conta corrente, conta poupança e DOC's.

Para que o Sistema gere dois arquivos separados por tipo de conta é necessário preencher a tabela **S052 - Parâmetros para CNAB/SISPAG** mencionada acima, caso contrário, o Sistema irá gerar um único arquivo com todos os tipos de conta.

Abaixo disponibilizamos 2 arquivos modelo padrão para pagamento de salários de acordo com o leiaute determinado para validação:

* Itaú: SISPAG – Modelo disponibilizado: “ItauFopag.pag”
* Bradesco: Modelo 2 – Modelo disponibilizado: “Bradesc.2pe"

**Saiba Mais**[Artigos CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
