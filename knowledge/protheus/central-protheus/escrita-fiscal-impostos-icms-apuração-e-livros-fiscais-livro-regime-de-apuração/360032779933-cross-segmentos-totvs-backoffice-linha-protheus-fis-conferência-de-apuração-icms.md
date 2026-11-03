---
article_id: 360032779933
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: 42dd1095c50adb55b5f7ee14c2da8744e7e33238e4bea510b16b315264ee2cd8
fetched_at: '2026-06-28T22:39:22.206077+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Conferência de Apuração
  (ICMS / ICMS-ST / IPI) MATA953
type: support-article
updated_at: '2022-03-14T20:10:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360032779933-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Confer%C3%AAncia-de-Apura%C3%A7%C3%A3o-ICMS-ICMS-ST-IPI-MATA953
---

**Duvida:**

Conferência de Apuração (ICMS/ICMS ST/IPI)

**Ambiente:**Microsiga Protheus - A partir da versão 12 Release 12.1.17.

**Solução:**

Observação: Para utilização desta funcionalidade a rotina MATA953 precisa estar com data igual ou superior a 30/04/2020.  
  
**Objetivo da Funcionalidade**Demonstrar todas as notas fiscais que compõem o valor carregado na apuração. Isso facilita a  
identificação de como foi realizado o cálculo dos impostos.   
Tela para conferência de valores nas abas **“Por Saídas/Prestações com Debito do Imposto”** e **“Por Entradas/Aquisições com Credito do Imposto”**.  
  
Habilita um *browser* com o detalhamento das notas fiscais e seus respectivos itens que compõem o valor listado na apuração.  
  
Este guia descreve como utilizar a ferramenta de conferência de apuração.  
  
**Importante:**

Para clientes que operam nas releases 12.1.27 ou anteriores, será necessária a execução do compatibilizador UPDDISTR com o pacote diferencial (SDFBRA.txt).

Esta correção também será disponibilizada na Expedição contínua de 05/2020 e o pacote poderá ser acessado através dos links disponibilizados na documentação **[Pacotes de Atualização - Fiscal](https://tdn.totvs.com/pages/viewpage.action?pageId=525823851).**

Informações sobre a Expedição contínua acessar: <http://tdn.totvs.com/x/H4uCEw>.  
Informações sobre o compatibilizador UPDDISTR acessar: [Atualizador de dicionário e base de dados - UPDDISTR](https://tdn.totvs.com/pages/viewpage.action?pageId=181965468).

Caso necessite, é possível criar o parâmetro **MV\_CONFAPU**manualmente:

|  |  |
| --- | --- |
| Nome | **MV\_CONFAPU** |
| Tipo | **Lógico** |
| Descrição | **Habilita a conferência da apuração de ICMS e ICMS-ST.** |
| Conteúdo | **.T.**- Habilita a opção de conferencia  **.F. -**Desabilita a opção de conferencia |

**Utilização**

Após realizar a apuração é necessário clicar no botão **"Outras Ações"** → **"Conf. Apuração ICMS / ICMS-ST"**

![](http://tdn.totvs.com/download/attachments/493630654/image2019-5-21_11-14-16.png?version=1&modificationDate=1558448180550&api=v2)

Ao clicar na opção **“Conf. Apuração ICMS e ICMS-ST”** é aberta uma tela para o escolher qual conferência deseja consultar.

![](http://tdn.totvs.com/download/attachments/493630654/image2019-5-21_11-14-47.png?version=1&modificationDate=1558448180520&api=v2)

Nesta tela é possível consultar as notas fiscais referente aos valores de débito e crédito do imposto de acordo com a opção selecionada. São visualizadas todas as notas fiscais de entrada/saída que compõem os valores de crédito/débito por nota fiscal da apuração. No segundo grid são listados os produtos relacionados com cada nota fiscal bem como os valores dos produtos e impostos.

![](http://tdn.totvs.com/download/attachments/493630654/image2019-5-21_11-15-49.png?version=1&modificationDate=1558448180330&api=v2)
