---
article_id: 360045206213
category: RH - RAIS
content_hash: 7b607bdf3f5fe3a91f6bde0b98244faf430982dfca29b5b30f78d0d8f92f1643
fetched_at: '2026-06-28T22:44:05.723975+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - Atualização RAIS 2020
type: support-article
updated_at: '2021-06-09T11:51:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045206213-RH-Linha-Protheus-GPE-Atualiza%C3%A7%C3%A3o-RAIS-2020
---

**Dúvida**Como será o envio da RAIS para funcionários com número de carteira de trabalho digital, visto que campo carteira de trabalho e série são obrigatórios dentro da manutenção de arquivo (GPEM510)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**

Em meados de outubro de 2019 o Ministério do Trabalho parou de realizar a impressão física da carteira de trabalho, passando a ser feita de forma digital levando em consideração o numero de CPF do trabalhador.  
Com isso é necessário ajustarmos na geração do magnético da RAIS para que leve a informação da carteira de trabalho corretamente.   
  
1º - Para clientes que possuir os campos RA\_NUMCP e RA\_SERCP **em branco**, devemos gerar no arquivo magnético da RAIS as informações da carteira de trabalho considerando o numero de CPF.

RAIS - número da CTPS com 7 dígitos + série 4 dígitos

Exemplo: numero de CPF: 69868015057

Vamos gerar na RAIS numero da CTPS: **69868015** e série: 00\*057\* vamos colocar zero a esquerda no magnético assim como já é feito hoje.  
  
2º - Para trabalhadores que possuírem os campos  RA\_NUMCP e RA\_SERCP **preenchidos**, vamos pegar essas informações para gerar as informações no magnético da RAIS.  
  
Segue abaixo os pacotes de atualização:  
12.1.27:<https://r.totvs.io/p/952789> ;  
12.1.25:<https://r.totvs.io/p/952788> ;   
12.1.23:<https://r.totvs.io/p/952787> ;  
12.1.17:<https://r.totvs.io/p/952786> ;  
  
**Importante:**Dentro da documentação é mencionado uma atualização de dicionário, a mesma estará disponível dentro do pacote acumulado que será liberado na terça-feira, dia 24/03. Sugerimos que os clientes, se possível esperem a atualização do dicionário para geração da Rais.  
Para os clientes que não puderem esperar, exite um procedimento paliativo dentro do boletim técnico para ser realizado via configurador - SIGACFG.  
  
**Saiba Mais**Para mais informações acesse o *link* a seguir: <https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030327-RH-RAIS>
