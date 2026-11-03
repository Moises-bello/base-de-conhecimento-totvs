---
article_id: 31430170765207
category: Entrada de dados
content_hash: 6ccb14ab20be32d1f0c705d1448fcc72d37b7d90f00473ed717bad0ddd12692f
fetched_at: '2026-06-28T22:46:30.541111+00:00'
product: rm
section_id: 1500000835061
source: central-rm
title: RH - RM - PTO -  Onde gerar o arquivo AFD - Arquivo Fonte de Dados
type: support-article
updated_at: '2025-10-22T00:51:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31430170765207-RH-RM-PTO-Onde-gerar-o-arquivo-AFD-Arquivo-Fonte-de-Dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31430176588567) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**O Automação de Ponto gera o arquivo AFD - Arquivo Fonte de Dados?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.80  
  
**Solução**

O Automação de Ponto não gera o arquivo **AFD (Arquivo Fonte de Dados)**, pois se trata de um sistema de tratamento das batidas, para onde as marcações são importadas (manualmente ou via integração), e não de um sistema de coleta, registro ou armazenamento das batidas.

Este arquivo é gerado pelos **REPs (Registradores Eletrônicos de Ponto),** que podem ser dispositivos físicos (relógios de ponto), aplicativos ou softwares em celulares, tablets e notebooks.   
  
Em caso de utilização dos dispositivos da Totvs abaixo segue os passo de como gerar o arquivo:  
  
Caso utilize a Clock in (Carol):   
[RH - Clock In by Carol - Obtendo o arquivo AFD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052559894)  
  
Caso utilize o app Meu RH:   
[RH - RM - Meu RH - Como gerar arquivo AFD da portaria 671 para o Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13728451898391)

Se o seu dispositivo for de **outro fabricante** e você tiver dúvidas sobre como gerar o arquivo, **entre em contato com o fabricante** para obter instruções detalhadas.

Abaixo segue as principais duvidas sobre o AFD:

O que é o **AFD**?   
O **AFD** é o arquivo onde ficam armazenados os detalhes das batidas registradas pelos funcionários nos REPs, seguindo a padronização da **Portaria 671 do Ministério do Trabalho**. Ele também pode ser identificado como o arquivo utilizado para **importar as marcações** para o Automação de Ponto, através do menu: Entrada de Dados | Importar,  informando no campo Arquivo para importação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31430170749591)

**Onde gerar o AFD?**

Através do próprio REP (Registrador Eletrônico de Ponto)

**Alguns REPs permitem a extração direta do AFD via:**

Pen drive (inserido no REP)

Comunicação serial ou USB (conectado a um computador)

Rede (Ethernet/Wi-Fi) (se o REP tiver essa funcionalidade)

**Via Software de Ponto Eletrônico**

Se a empresa usa um sistema de ponto eletrônico integrado, o AFD pode ser gerado pelo software, geralmente em:

Menu "Relatórios" ou "Exportar AFD"

Formato .txt ou.afd (padrão MTE)

**Empresas Terceirizadas (Caso não tenha suporte interno)**

Algumas empresas terceirizam a gestão do ponto e fornecem o AFD automaticamente.  
  
**Saiba Mais:**  
[RH - RM - PTO - Tipos de REPs (Registros Eletrônicos de Ponto) de acordo com a Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22760840044183)

[Registro Eletrônico de Ponto - REP](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/fiscalizacao-do-trabalho/rep)

[Leiaute do Arquivo Fonte de Dados - AFD (art. 81,caput, da Portaria n° 671/2021) - 08/06/2022](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/fiscalizacao-do-trabalho/leiaute-do-arquivo-fonte-de-dados-afd.pdf)

[PORTARIA MTP Nº 671, DE 8 DE NOVEMBRO DE 2021](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/legislacao/portarias-1/portarias-vigentes-3/portaria-no-671-de-8-de-novembro-de-2021-compilada-20-10-2023.pdf/@@download/file)
