---
content_hash: 2258148f2cd8e771f90a3f31130ad6b3dbefa5b23fe95e3c13075fa7654861f6
fetched_at: '2026-06-29T00:05:58.435706+00:00'
page_id: '187531511'
product: rm
source: tdn-rm
title: Emissão de boletos no portal do Aluno - Gerador.net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=187531511
version: 8
---

Boleto para emissão no portal do Aluno [Corpore.net](http://Corpore.net)

**1) FÓRMULA CÓDIGO BARRAS:**

---

Deverá ser criada a fórmula CODBARRABOLETO(-1), conforme imagem abaixo:

Clique aqui para exibição da imagem

**OBS:** **Esta formula deverá ser cadastrada para o aplicativo RM FLUXUS – TOTVS GESTÃO FINANCEIRA.**

**2) FÓRMULA IPTE BOLETO:**

---

Deverá ser criada a fórmula IPTEBOLETO(-1), conforme imagem abaixo:

Clique aqui para exibição da imagem

**OBS:** **Esta formula deverá ser cadastrada para o aplicativo RM FLUXUS – TOTVS GESTÃO FINANCEIRA.**

**3) CRIAÇÃO DA CONSULTA SQL:**

---

Será necessário incluir a consulta SQL que retorne o resultado da fórmula criada.

Abaixo a sintaxe da consulta:

***SELECT CONVERT( VARCHAR(100), :CODBAR) AS BOLETO***

***FROM FLAN(NOLOCK)***

***WHERE FLAN.CODCOLIGADA = :CODCOLIGADA***

***AND FLAN.IDBOLETO = :IDBOLETO***

Clique aqui para exibição da imagem

***OBS: Deverá se atentar que a consulta SQL deverá ser cadastrada selecionando o aplicativo TOTVS Gestão Financeira***

**4) INCLUSÃO DO RELATÓRIO:**

---

No MENU Gestão inclua um novo relatório.

Clique aqui para exibição da imagem

O relatório deverá ter a sua tabela Master definida como FLAN:

Clique aqui para exibição da imagem

Adicione os campos (CODCOLIGADA e IDBOLETO) da tabela FLAN

Clique aqui para exibição da imagem

Os campos CODCOLIGADA e IDBOLETO, devem estar presentes no detalhe do relatório.

**5) INSIRA O COMPONENTE CÓDIGO DE BARRAS**:

---

Clique aqui para exibição da imagem

**6) REALIZE A CONFIGURAÇÃO NAS PROPRIEDADES DO CÓDIGO DE BARRAS:**

---

Clique aqui para exibição da imagem

**7) DEVERÁ SER ALTERADO NAS PROPRIEDADES O NOME DO DESENHO RESPECTIVO AO CAMPO INSERIDO.**

---

Clique aqui para exibição da imagem

Este nome deverá ser o mesmo que foi referenciado na consulta SQL utilizada no relatório.

Abaixo segue um exemplo onde o nome do desenho referenciado ao campo do relatório foi alterado para o mesmo existente na consulta SQL utilizada.

**8) INSERINDO AS FÓRMULAS NO RELATÓRIO (COD.BARRAS E IPTE)**

---

Clique aqui para exibição da imagem

**9) DEVERÁ SER ALTERADO NAS PROPRIEDADES O NOME DO DESENHO RESPECTIVO AO CAMPO INSERIDO.**

---

Este nome deverá ser o mesmo que foi referenciado na consulta SQL utilizada no relatório.

Abaixo segue um exemplo onde o nome do desenho referenciado ao campo do relatório foi alterado para o mesmo existente na consulta SQL utilizada.

Clique aqui para exibição da imagem

**10) SALVE ESTAS PARAMETRIZAÇÕES NO RELATÓRIO E EXECUTE O MESMO EM SEGUIDA.**

---

**11) INFORMA O RELATÓRIO NOS PARÂMETROS DO SISTEMA CONFIGURAÇÕES -> PARÂMETROS -> TESOURARIA ->****RELATÓRIOS**

---

Acessar o menu de parametrização do relatório criado e informar o relatório utilizado para emissão do boleto via portal

Clique aqui para exibição da imagem

**12) ACESSAR O PORTAL ACADEMICO PARA EMISSÃO DE BOLETO**

---

Acessar o portal com o usuário de um aluno para emissão do boleto.

Clique aqui para exibição da imagem
