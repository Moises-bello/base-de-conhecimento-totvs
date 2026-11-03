---
article_id: 360057926754
category: GPE - eSocial - Periódicos
content_hash: 77541b9ece4d73f3d4792fe46903d19f559ac354eb91b16b67580ec26df309bc
fetched_at: '2026-06-28T22:45:08.735342+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - Para que serve e como utilizar
  o parâmetro MV_RATESOC na geração do evento S-1200
type: support-article
updated_at: '2025-07-17T14:32:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057926754-RH-Linha-Protheus-GPE-eSocial-S-1200-Para-que-serve-e-como-utilizar-o-par%C3%A2metro-MV-RATESOC-na-gera%C3%A7%C3%A3o-do-evento-S-1200
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33533573102231) Tempo aproximado para leitura: 00:05:00 min**

**Dúvida**  
Para que serve e como utilizar o parâmetro MV\_RATESOC na geração do evento S-1200?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O parâmetro **MV\_RATESOC** serve para definir se o S-1200 será gerado com o centro de custo do movimento da folha, ou com o centro de custo do cadastro do funcionário (SRA).  
  
Quando o trabalhador teve o calculo em mais de um **centro de custo o S-1200** é gerado de forma **rateada**, pois entende-se que as tributações devem ser rateadas entre a lotações tributarias. Caso o parâmetro esteja desabilitado o S-1200 será gerado sem o rateio das informações. Nesse caso antes de modificar o parâmetro cabe ao empregador analisar as aplicações legais de gerar ou não gerar o S-1200 sem o rateio.  
**Exemplo:**O centro de custo do cadastro do funcionário é o **9.09.01**, cujo cadastro na tabela CTT o define como um CNO, sob inscrição **123456**. A filial do funcionário possui tipo de inscrição de CNPJ, de inscrição **53.113.791/0001-22.**

A folha do funcionário de 07/2019 possui, de forma resumida, os lançamentos abaixo:

| Verba | Descrição | Valor | Centro de Custo |
| --- | --- | --- | --- |
| 112 | Salário | R$ 4.000,00 | 1.01.01 |
| 112 | Salário | R$ 4.000,00 | 1.01.02 |
| 417 | INSS Folha | R$ 321,16 | 1.01.01 |
| 417 | INSS Folha | R$ 321,17 | 1.01.02 |

**OBS:** os centros de custo **1.01.01** e **1.01.02** não estão cadastrados como CNO.  
  
Ao efetuar a geração do evento S-1200, o sistema irá efetuar a geração dos estabelecimentos conforme o exemplo abaixo:  
  
**1º** - Parâmetro **MV\_RATESOC** configurado com **.T.** ou se **NÃO**existir no dicionário SX6:

| Tipo de Inscrição | Inscrição | Lotação |
| --- | --- | --- |
| 1 | 53113791000122 | 1.01.01 |
| 1 | 53113791000122 | 1.01.02 |

Rubricas geradas:

| Lotação | Rubrica | Valor |
| --- | --- | --- |
| 1.01.01 | 112 | R$ 4.000,00 |
| 1.01.01 | 417 | R$ 321,16 |
| 1.01.02 | 112 | R$ 4.000,00 |
| 1.01.02 | 417 | R$ 321,17 |

**2º** - Parâmetro **MV\_RATESOC** configurado com **.F.**:

| Tipo de Inscrição | Inscrição | Lotação |
| --- | --- | --- |
| 4 | 123456 | 9.09.01 |

  
Rubricas geradas:  

| Lotação | Rubrica | Valor |
| --- | --- | --- |
| 9.09.01 | 112 | R$ 8.000,00 |
| 9.09.01 | 417 | R$ 642,33 |

**Importante:**  
O funcionamento padrão do sistema é efetuar a geração dos estabelecimentos conforme o centro de custo do movimento da folha. Caso deseje alterar o conceito e efetuar a geração de acordo com o centro de custo do cadastro do funcionário, é necessário efetuar a inclusão **manualmente** do parâmetro no módulo SIGACFG - Configurador.  
  
**Aviso:**

Ao configurar o parâmetro MV\_RATESOC com .F., a configuração criada conforme documentação documentação [DRHESOCP-12005 DT Novo Controle de Lotações](https://tdn.totvs.com/pages/viewpage.action?pageId=489760572) será desativada, uma vez que a configuração do parâmetro com falso define que os estabelecimentos devem ser gerados a partir do centro de custo do cadastro do funcionário.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[Parâmetro MV\_RATESOC](https://tdn.totvs.com/pages/viewpage.action?pageId=502841845)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
