---
article_id: 360035623713
category: RH - CNAB
content_hash: d9a793c024d47fde8e88d23dc26428b28413ff82872e00c0e16424935c70a34c
fetched_at: '2026-06-28T22:43:39.184478+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar arquivo CNAB para beneficiários de pensão
  alimentícia
type: support-article
updated_at: '2025-09-19T18:51:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035623713-RH-Linha-Protheus-GPE-Como-gerar-arquivo-CNAB-para-benefici%C3%A1rios-de-pens%C3%A3o-aliment%C3%ADcia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32852136339351) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como gerar arquivo CNAB para beneficiários de pensão alimentícia?

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.

**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. **Acesse Atualizações > Funcionários > Beneficiários** e efetue o cadastro do beneficiário, informando conta e agência de pagamento:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045663094)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045663694)

2. Execute o cálculo da folha de pagamento, verificando o desconto da pensão nos cálculos:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046516973)

3. Acesse **Miscelânea > Líquido > Geração de Arquivo Líquido** e configure o grupo de perguntas da rotina de acordo com os cálculo realizado. No exemplo abaixo, faremos de uma matrícula específica:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8337212395159)  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8337444315543)  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046521233)  
  
  
4. Será apresentado o relatório de líquidos com as informações do beneficiário (**Filial / Banco-Agência / Matrícula / Funcionário / Valor**)   
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045674034)  
  
5. Selecione o diretório especificado no grupo de perguntas, e abra o arquivo CNAB gerado para visualizar as informações geradas:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045674594)

**Observações:**  
1) A verba utilizada para cálculo de pensão e cadastrada no cadastro de beneficiários não pode possuir identificador de cálculo.  
2) As verbas configuradas no cadastro de beneficiários não podem ser iguais pois podem gerar duplicidades na geração do arquivo de líquido e do arquivo CNAB.   
3) Caso após a geração o arquivo txt apresente o nome do funcionário e não o nome do beneficiário, será necessário revalidar o arquivo de configuração, pois pode ter sido configurado apenas para busca da SRA e neste caso não trata o nome do beneficiário. Como apoio verifique o arquivo disponível anexo a esta documentação. 

**Importante:**  
Para a realização das configurações e validações do arquivo **CNAB,** indicamos que seja acionado o ESN, para análise e orçamento de um analista in loco ou HUB, uma vez que o suporte padrão não oferece auxílio em customizações. Porém, caso o cliente tenha conhecimento, abaixo, disponibilizamos 2 arquivos CNAB modelo padrão para validação. 

**Saiba Mais:**

[RH - Linha Protheus - GPE - Como configurar o título de pensão automaticamente com dados do beneficiário como fornecedor](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025329234-RH-Linha-Protheus-GPE-Como-configurar-o-t%C3%ADtulo-de-pens%C3%A3o-automaticamente-com-dados-do-benefici%C3%A1rio-como-fornecedor-?source=search)

[RH - Linha Protheus - GPE - Passo a passo para geração do Arquivo CNAB (GPEM080)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8420406092951-RH-Linha-Protheus-GPE-Passo-a-passo-para-gera%C3%A7%C3%A3o-do-Arquivo-CNAB-GPEM080-)

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
