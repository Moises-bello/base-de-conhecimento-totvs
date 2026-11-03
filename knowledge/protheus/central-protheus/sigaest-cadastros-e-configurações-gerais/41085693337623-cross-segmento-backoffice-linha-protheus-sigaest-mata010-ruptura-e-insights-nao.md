---
article_id: 41085693337623
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 519c7bd453d47149dd5c0dd7a1c99244bfc2b13463840cc14b63b6bd942fc779
fetched_at: '2026-06-28T22:39:09.546306+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Ruptura
  e Insights nao foi possivel gerar modelo por falta de dados
type: support-article
updated_at: '2026-06-09T14:11:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41085693337623-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Ruptura-e-Insights-nao-foi-possivel-gerar-modelo-por-falta-de-dados
---

A mensagem "não há dados disponíveis" na Central de IA, opção Ruptura do cadastro de produto, ocorre por falta de dados ou atualizações. O Protheus Insights funciona apenas em ambiente de produção, com modelos treinados aos finais de semana. Verifique pacotes atualizados, envie registros das tabelas solicitadas e valide a data da lib para suporte.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41085679106967) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao acessar a Central de IA, na opção Ruptura do **cadastro de produto**, o sistema exibe a mensagem informando que não há dados disponíveis, ou não foi possível gerar modelo por falta de dados.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Falta de atualizações ou dados insuficientes para apresentação dos insights  
  
**Solução**  
A funcionalidade Protheus Insights está disponível e operacional **apenas no ambiente de produção**. Não configure em ambiente teste.

Os modelos são treinados aos finais de semana, ou seja, se a movimentação ocorrer durante a semana, só será processada na próxima segunda-feira.

Guia para configuração correta dos Insights: <https://tdn.totvs.com/x/QzicMg>

**1. Verifique se está com o pacote de expedição continuada atualizado:**

* INSIGHTS\_EXPEDICAO\_CONTINUA: <https://tdn.totvs.com/x/eoNHOQ>

**2. Caso não seja cliente Cloud, nos envie os registros das duas últimas semanas das tabelas:**

* Cópia das tabelas I14, I19 e I21 no formato SQLite;
* Cópia da tabelas SX3 (Filtrando os campos das tabelas I14, I19 e I21);
* Cópia da tabela SYS\_COMPANY.

**4. Nos encaminhe o ID da Central de Diagnósticos:**

* How To | Central de Diagnóstico - Como enviar dados ao Suporte? (<https://youtu.be/UHiwrwF1smA?si=NuYC2q7CHyXjxJ-6>)

**5. Valide se a data da lib está atualizada em seu ambiente**

* LIB\_LABEL: <https://tdn.totvs.com/x/9YUbCQ>

Encaminhe todas essas informações ao suporte padrão, para que possa ser acionado o time correspondente, caso seu ambiente esteja devidamente atualizado.

**Saiba mais:**

[*Clique aqui para mais informações sobre a MATA010*](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
