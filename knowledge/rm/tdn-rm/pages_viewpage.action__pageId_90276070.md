---
content_hash: 38c6404a1009a3cee48d14f38f43321a3c4daf5a1896bc08f2c2d04ed4776ef4
fetched_at: '2026-06-29T00:12:02.685054+00:00'
page_id: '90276070'
product: rm
source: tdn-rm
title: Como incluir código de Barras em relatórios do tipo boleto (reports)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=90276070
version: 11
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Reports                         **Versão:**11.82 |
| **Processo** | **:** | Criação de código de barras |
| **Subprocesso** | **:** | Código de Barras |
| **Data da publicação** | **:** | 13/08/2014 |

Para realizar a inclusão de Códigos de Barras em relatórios deve-se realizar o seguinte procedimento:

**1) FÓRMULA CÓDIGO BARRAS:**

Deverá ser criada a fórmula CODBARRABOLETO(-1), conforme imagem abaixo:

**OBS:** **Esta formula deverá ser cadastrada para o aplicativo RM FLUXUS – TOTVS GESTÃO FINANCEIRA.**

**2) FÓRMULA IPTE BOLETO:**

Deverá ser criada a fórmula IPTEBOLETO(-1), conforme imagem abaixo:

**OBS:** **Esta formula deverá ser cadastrada para o aplicativo RM FLUXUS – TOTVS GESTÃO FINANCEIRA.**

**3) CRIAÇÃO DA CONSULTA SQL:**

Será necesário incluir a consulta SQL que retorne o resultado da fórmula criada.

Abaixo a sintaxe da consulta:

***SELECT CONVERT( VARCHAR(100), :CODBAR) AS BOLETO***

***FROM FLANBOLETO(NOLOCK)***

***WHERE FLANBOLETO.CODCOLIGADA = :CODCOLIGADA***

***AND FLANBOLETO.IDBOLETO = :IDBOLETO***

*****OBS:** Deverá se atentar que a consulta SQL deverá ser cadastrada selecionando o aplicativo RM Fluxus***

**4) INCLUSÃO DO RELATÓRIO:**

No MENU Gestão inclua um novo relatório.

Este relatório devera ter a sua tabela definida como FLANBOLETO:

Adicione a Tabela (IDBOLETO)

Os campos CODCOLIGADA e REFERENCIA DO BOLETO, devem estar presentes no detalhe do relatório.

**5) INSIRA O COMPONENTE CÓDIGO DE BARRAS**:

**6) REALIZE A CONFIGURAÇÃO NAS PROPRIEDADES DO CÓDIGO DE BARRAS:**

**7) INSERINDO AS FÓRMULAS NO RELATÓRIO (COD.BARRAS E IPTE)**

**8) DEVERÁ SER ALTERADO NAS PROPRIEDADES O NOME DO DESENHO RESPECTIVO AO CAMPO INSERIDO.**

Este nome deverá ser o mesmo que foi referenciado na consulta SQL utilizada no relatório.

Abaixo segue um exemplo onde o nome do desenho referenciado ao campo do relatório foi alterado para o mesmo existente na consulta SQL utilizada.

OBS: O mesmo deverá ser válido para o campo **REFERENCIADO BOLETO (IDBOLETO)**

**9) SALVE ESTAS PARAMETRIZAÇÕES NO RELATÓRIO E EXECUTE O MESMO EM SEGUIDA.**

|  |  |
| --- | --- |
|  |  |
