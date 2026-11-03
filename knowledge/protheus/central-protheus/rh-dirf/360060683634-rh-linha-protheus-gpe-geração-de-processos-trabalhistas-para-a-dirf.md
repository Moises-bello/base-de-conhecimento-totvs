---
article_id: 360060683634
category: RH – DIRF
content_hash: ad660e71ae86c7c012f154c2c27baa6c8428ac971e39e8b9d4a557e2f89a101e
fetched_at: '2026-06-28T22:44:07.013258+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Geração de Processos trabalhistas para a DIRF
type: support-article
updated_at: '2026-06-17T20:14:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060683634-RH-Linha-Protheus-GPE-Gera%C3%A7%C3%A3o-de-Processos-trabalhistas-para-a-DIRF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34302179780503) Tempo aproximado para leitura: **00:03:00 min**  
**Ocorrência**Geração de Processos Trabalhistas para a DIRF.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**As empresas passam a ser obrigadas a informar na DIRF os valores correspondentes a Processos judiciais, seja da Justiça do Trabalho, Justiça Estadual ou Justiça Federal, mesmo que os rendimentos não tenham sofridos retenção.

Esse processo já existia na DIRF, mas só era declarado em casos onde ocorreu retenção. A partir de 2020 a Receita Federal informa que deverá ser declarado em ambos os casos.  
  
**Solução**  
Esses valores não transitam pela Folha de Pagamento, desta forma, não podem ser integrados automaticamente. Abaixo seguem orientações de como informar esses dados para a DIRF.  
  
Exemplo de declaração:

Indicamos aos nossos usuários que utilizem:

* **Próprio programa Gerador e Validador da DIRF**.  
  OU
* **Informar na nossa rotina de Manutenção da DIRF (GPEM560) os valores referentes a esses processos.**

**Inserindo as informações diretamente no Protheus:**

1. Inserir na tabela de Códigos de Retenção do Imposto de Renda os códigos referentes aos rendimentos decorrentes de decisão judicial.  
No módulo Configurador, SIGACFG, acesse Ambiente → Cadastros → Tabelas  
Na rotina de Tabelas Genéricas posicione na tabela 37 e clique em editar:  
![](https://tdn.totvs.com/download/attachments/587833444/image2021-1-12_16-44-29.png?version=1&modificationDate=1610480669687&api=v2)  
  
2. Inclua as as seguintes informações:

**1895**- Rendimentos Decorrentes de Decisão da Justiça dos Estados/Distrito Federal, exceto o disposto no art. 12-A da Lei nº 7.713, de 1988   
**5928**- Rendimentos decorrentes de decisão da Justiça Federal, exceto o disposto no art. 12-A da Lei nº 7.713, de 1988   
**5936**- Rendimentos Decorrentes de Decisão da Justiça do Trabalho, exceto o disposto no art. 12-A da Lei nº 7.713, de 1988  
  
Após inclusão, clique no botão de **Confirmar**, conforme abaixo:  
![](https://tdn.totvs.com/download/attachments/587833444/image2021-1-12_16-54-58.png?version=1&modificationDate=1610481298627&api=v2)  
  
3. No Gestão de Pessoal (SIGAGPE) faça a geração de dados da DIRF utilizando a rotina **Gerar Arquivo** pelo caminho **>Miscelânea >Dirf >Gerar Arquivo**;  
  
4. Na rotina de **Manutenção do Arquivo**, pelo caminho **>Miscelânea >Dirf >Manutenção Arquivo,** inclua um novo registro com as informações do processo:  
**Matrícula:** Informe o código do beneficiário, não necessariamente precisa estar na tabela SRA, neste caso gere um código de controle a seu critério.  
**Código de Retenção**: 1895, 5928 ou 5936, cadastrados anteriormente.  
Preencher os demais campos conforme orientação do help e informe os valores referente ao processo em questão.  
![](https://tdn.totvs.com/download/attachments/587833444/image2021-1-12_16-49-24.png?version=1&modificationDate=1610480964830&api=v2)  
  
5. Gere o **Arquivo Magnético** pelo caminho **>Miscelânea >Dirf >Arquivo Magnético** utilizando a rotina.

**Inserindo as informações diretamente no Validador da DIRF 2021**  
**Exemplo 1 - para Pessoas****Jurídicas****(exceto Instituições Financeiras)**

1. As informações de Processos podem ser informadas na Ficha de Rendimentos Tributáveis, informando a identificação do beneficiário (CPF, Nome), Código de Receita e Valores Pagos referente ao Processo:  
![](https://tdn.totvs.com/download/attachments/587833444/image2021-1-15_15-20-38.png?version=1&modificationDate=1610734838337&api=v2)

**Exemplo 2 - para Instituições****Financeiras**

2. Selecione a opção referente a Instituição Financeira:  
![](https://tdn.totvs.com/download/attachments/587833444/image2021-1-13_16-58-37.png?version=1&modificationDate=1610567917283&api=v2)  
  
Ao confirmar, será apresentada a opção de **Justiça do Trabalho/Federal/Estadual/Distrito Federal:**  
![](https://tdn.totvs.com/download/attachments/587833444/image2021-1-13_17-0-1.png?version=1&modificationDate=1610568000710&api=v2)  
  
Realize o preenchimento dos campos conforme menus **Beneficiários**, **Rendimentos Tributáveis** e **Rendimentos Recebidos Acumuladamente**:  
![](https://tdn.totvs.com/download/attachments/587833444/image2021-1-13_17-2-34.png?version=1&modificationDate=1610568159457&api=v2)  
![](https://tdn.totvs.com/download/attachments/587833444/image2021-1-13_17-8-32.png?version=1&modificationDate=1610568512170&api=v2)  
  
**Importante:** Os dados de número do processo, tipo do processo (Justiça do Trabalho, Federal ou Justiça Estadual ou do Distrito Federal) e referentes ao Advogado/Escritório de Advocacia, devem ser prestados pelas Instituições Financeiras que, na condição de depositárias de crédito, conforme arts. 27 e 28 da Lei nº 10.833, de 2003, efetuaram pagamentos de rendimentos decorrentes de decisão da Justiça do Trabalho (código 5936), Justiça Federal (código 5928) ou Justiça Estadual ou do Distrito Federal (1895) sujeitos à retenção do imposto sobre a renda. Desta forma, a ficha PROC, não constará no TXT gerado pelo nosso programa.

**Saiba mais**  
[Dados de Processos na DIRF](https://tdn.totvs.com/display/PROT/Dados+de+Processos+na+DIRF)

[Página centralizadora Protheus - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
