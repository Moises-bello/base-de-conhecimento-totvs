---
article_id: 360013664351
category: Portal
content_hash: 2644e4506c4ddea3ce78bf6f550472c165b41f8d0ed9b39643c57cb521b251c6
fetched_at: '2026-06-28T22:46:37.907252+00:00'
product: rm
section_id: 1500000835141
source: central-rm
title: RH - RM - PTO - Erro ao inserir batidas no portal para funcionário de férias
type: support-article
updated_at: '2026-03-16T17:03:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013664351-RH-RM-PTO-Erro-ao-inserir-batidas-no-portal-para-funcion%C3%A1rio-de-f%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16512166014615) Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**

Ao inserir batidas para funcionário que esteve de férias dentro do período atual e ativo aparece a mensagem *"Ocorreu um erro ao efetuar a leitura do registro: Funcionário em período de férias na data e/ou período selecionada."* O que fazer ?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.18  
  
**Solução**

Houve uma melhoria a partir das versões 12.1.18.197/ 12.1.19.151 / 12.1.20.104 e superiores, referente ao processo de inserir batidas no portal para funcionários que está de férias eu esteve férias parciais dentro do período ativo. Segue abaixo o posicionamento do desenvolvimento:  
  
*'Foi incluída validação se a data ou período selecionado para a inclusão de batidas pelo funcionário através do Portal WEB está contido no período de gozo de férias, caso esteja o sistema não permitirá a inclusão.*

*Observação: Caso o funcionário selecione datas que não estejam contidas no período de gozo de férias o mesmo poderá proceder com a inclusão das batidas, porém se pelo menos uma data estiver contida no período de gozo o sistema não permitirá a inclusão, o mesmo ocorrerá caso nenhuma data seja selecionada e o período possua interseção com o período de gozo.*  
  
*Abaixo segue mensagem que será apresentada caso a data e/ou período selecionado esteja contido no período de gozo de férias:*  
  
*"Funcionário em período de férias na data e/ou período selecionado."*  
  
  
Para inserir batidas quando há férias parciais no portal, acesse a edição do espelho de ponto do subordinado. Selecione o dia no qual deseja incluir a batida e acesse o menu Anexo/Entrada de batidas e incluir a batida no dia selecionado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009353852)
