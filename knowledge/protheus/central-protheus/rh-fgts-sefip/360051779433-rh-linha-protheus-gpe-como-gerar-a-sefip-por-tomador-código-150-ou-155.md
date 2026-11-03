---
article_id: 360051779433
category: RH - FGTS / SEFIP
content_hash: c091ed9449076de03a1b5acc1f9730f7f9c8b81a464af78be341ce5a225f84d7
fetched_at: '2026-06-28T22:43:41.337532+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: 'RH - Linha Protheus - GPE -  Como gerar a SEFIP por tomador código 150 ou
  155 '
type: support-article
updated_at: '2025-08-07T13:40:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051779433-RH-Linha-Protheus-GPE-Como-gerar-a-SEFIP-por-tomador-c%C3%B3digo-150-ou-155
---

**Dúvida**:  
Como gerar a SEFIP por tomador código 150 ou 155?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Configuração da SEFIP com código de **Recolhimento 155** (por CEI) ou **150** (CNPJ), por Tomador de Serviço:  
No módulo de Gestão de Pessoal, o tomador é representado pelo cadastro de **Centro de Custo**. Por isso, devem ser criados Centros de custo para os tomadores, e pela rotina **Transferência**, alocar o funcionário no tomador no qual ele trabalhou. Quando quiser trocar o tomador, deve fazer nova transferência.

No cadastro de **Centro de Custo**, pelo caminho **>Atualizações >Cadastros >Centro de Custos**, o centro de custos correspondente ao tomador deve estar com seus respectivos **CEIs** ou **CNPJ** informados na aba Tomador, além do endereço, nome e demais informações, conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405969913879/mceclip0.png)

Caso alguns funcionários não tenham que constar no tomador, e tenha que estar na própria empresa (funcionários do setor administrativo por exemplo), eles devem estar alocados num Centro de Custo cujo campo **Inscrição no CNPJ/CEI** esteja em branco. Desta forma o CNPJ levado será o que está informado na própria empresa (SIGAMAT).

Resumindo a etapa anterior, os únicos Centro de Custos que devem ter com os campos **CNPJ/CEI** preenchidos são os **Centro de Custos** vinculados ao **Tomador de Serviço**.  
  
**Observação**:   
Em **>Atualizações >Definições de cálculo >Manutenção de tabelas** (as tabelas S037 e S038), o código de **Terceiros** deve sempre estar compatível com o **FPAS** (o campo **código FPAS** encontra-se no cadastro da empresa).

Feito isso o sistema está pronto pra gerar a SEFIP no **código de recolhimento 155**ou**150**.  
  
Deve-se observar algumas perguntas da geração do arquivo SEFIP:  
- A pergunta **Gerar Sefip Por** deve estar como **Centro de Custo**, o Código de GPS da Filial deve ser informado 2100 ou 2003, 2003 se for optante pelo SIMPLES, e o código 2100 se não for.  
- O código de pagamento da GPS do Centro de Custo deve ser 2208 obrigatoriamente quando o código de recolhimento for 155.  
- Se for 2100 ou 2003, o Código da GPS do Centro de custo deve ser o mesmo usado para a GPS da Filial, ou seja 2003 ou 2100.  
**Saiba mais:**<https://tdn.totvs.com/display/public/PROT/FGTS>
