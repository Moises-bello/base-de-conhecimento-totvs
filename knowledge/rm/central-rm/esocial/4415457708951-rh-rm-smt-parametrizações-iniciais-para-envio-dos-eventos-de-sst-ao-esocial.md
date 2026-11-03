---
article_id: 4415457708951
category: eSocial
content_hash: 64c2369e49d9e71c7d91cee66ab1bc25ae2748d60a9f5a003640943413ec5385
fetched_at: '2026-06-28T22:47:39.102252+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: RH - RM - SMT - Parametrizações Iniciais para envio dos eventos de SST ao eSocial
type: support-article
updated_at: '2024-10-08T14:33:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415457708951-RH-RM-SMT-Parametriza%C3%A7%C3%B5es-Iniciais-para-envio-dos-eventos-de-SST-ao-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035736407063) Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Quais a parametrizações iniciais para realizar o envio dos eventos de SST ao eSocial ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Segurança e Saúde Ocupacional - 12.1.31 e superiores.  
  
**Solução**Abaixo segue as parametrizações iniciais que devem ser realizadas:

**1.** Acesse o módulo de **Folha de Pagamento | Configurações** | **Parametrizador** | **Etapa eSocial** | **Configurações Gerais 1/7**, avalie se o campo 'Versão do Leiaute' está sempre com o Leiaute atual do eSocial para envio dos eventos.

[Leiautes do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26919595575575)

**2.** Ainda no parametrizador da **Folha de Pagamento** | **Etapa eSocial** | **Configurações gerais 1/7**, avalie se a **Data de Obrigatoriedade/Adesão ao eSocial**no campo **Saúde e Segurança do Trabalhador** está preenchida, seguindo o cronograma do eSocial para o grupo da Empresa.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26919595577367)

Cronograma eSocial:

![Cronograma eSocial](https://www.gov.br/receitafederal/pt-br/arquivos-e-imagens/noticias-do-site/cronograma_esocial-1.jpg)

**3****.** Acesse o módulo de **Segurança e Saúde Ocupacional** | **Opções** | **Parametrizador** ao abrir o assistente clique em avançar, e selecione a etapa**Profissiografia** e selecione um ou mais itens.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26919579432983)  
**Obs.: Este item é responsável por levar a descrição das atividades no evento S-2240.**  
  
**4.** E no parametrizador do SSO na etapa **eSocial - SST** | **Etapa 2 - Condições Ambientais de Trabalho,** defina se os EPI's, serão considerados do fornecimento aos funcionários ou se serão considerados através do vinculo ao risco, nível do risco e  avaliação de risco. Caso a flag, **consiste EPI através de Associação ao Risco, Nível de Risco e Avaliação de Risco** esteja **desmarcada** o EPI só será considerado a partir do fornecimento ao funcionario.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26919595583511)

**Obs.: Este item é responsável para levar o EPI ao evento S-2240.**  
  
**Saiba Mais:**

Para maiores informações, acesse:

- [RH - RM - SMT - Evento S-2210 - CAT (Comunicação de Acidente de Trabalho)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028898652)

- [RH - RM - SMT - Gerar o evento S-2220 - Monitoramento da Saúde do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010325282)

- [RH - RM - SMT - Gerar o evento S-2221 - Exame Toxicológico do Motorista Profissional Empregado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25679917455255)

- [RH - RM - SMT - Gerar o evento S-2240 - Condições Ambientais do Trabalho - Fatores de Risco](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007674022)
