---
article_id: 1500000048961
category: Avaliação e Pesquisa de Desempenho (SIGAAPD)
content_hash: db94558a49e96703958b3f250c72b771c7f9ba08016faf2b19e44bfd00642837
fetched_at: '2026-06-28T22:42:53.911488+00:00'
product: protheus
section_id: 206956088
source: central-protheus
title: RH - Linha Protheus -  APD - No relacionamento de participantes (APDA020) como
  realizar um filtro nos registros que serão relacionados ou atualizados
type: support-article
updated_at: '2021-04-06T19:48:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000048961-RH-Linha-Protheus-APD-No-relacionamento-de-participantes-APDA020-como-realizar-um-filtro-nos-registros-que-ser%C3%A3o-relacionados-ou-atualizados
---

**Dúvida**No relacionamento de participantes (APDA020) é possível realizar um filtro nos registros que serão relacionados ou atualizados?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Avaliação Pesquisa e Desempenho – Todas as versões  
  
**Solução**Esta rotina é utilizada por vários módulos do Protheus, como Ativo Fixo, Gestão de Pessoal, Avaliação e Pesquisas de Desempenho, Acompanhamento de Processos Trabalhistas, Login no Portal GCH, entre outros.  
  
Seu principal objetivo é cadastrar pessoas que mantêm algum tipo de relacionamento com a empresa, que podem ser, por exemplo, funcionários ou prestadores de serviços.  
  
Realizado tratamento no cadastro de participantes permitindo que o usuário filtre por filial, matricula, data de admissão e categoria.  
  
Para essa finalidade foi criado o grupo de perguntas **APD20UPDRA**.  
  
A melhoria estará disponível a partir da versão **12.1.17**, mas caso esteja utilizando uma versão anterior à **12.1.27** o grupo de perguntas deverá ser criado de **forma manual no configurador**. Caso esteja em uma versão superior ou igual a **12.1.27 a criação acontecerá automaticamente** na atualização de release.  
  
Para o correto funcionamento da rotina é necessário possuir o grupo de perguntas **APD20UPDRA** em seu ambiente, seguem dados para sua criação manual caso esteja nos releases **12.1.17/ 12.1.23 ou 12.1.25.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000049602/mceclip0.png)  
  
1.** Para executar a rotina, acesse o Módulo 53 **(SIGAAPD)**, no seguinte Caminho: **Atualizações > Cadastro > Participante > Outras ações > Relacionar.**  
**2.** Seleciona a opção desejada **Relacionar / Atualizar / ou Ambos** e confirme o processamento clicando em **Salvar**.  
**3.** Será apresentado o novo grupo de perguntas permitindo que seja aplicado filtros no relacionamento, após seleção conforme necessidade da empresa.  
**4.** Confira os dados e confirme a inclusão.  
  
![Hm75aMtJ8Z.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101138513/Hm75aMtJ8Z.gif)  
  
**Saiba Mais**  
[Como relacionar os Participantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051031874)  
[Qual a diferença das opções "Relacionar, Atualizar e Ambos" do cadastro de Participantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052360593)  
[Artigos Portal Gestão Capital Humano](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano%C2%A0%20)  
[Artigos Avaliação Pesquisa e Desempenho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206956088-RH-Avalia%C3%A7%C3%A3o-e-Pesquisa-de-Desempenho)
