---
article_id: 360013152511
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 6ad79f407d941496860968630409bcf90e85a44f05411012e96170622cf80dc8
fetched_at: '2026-06-28T22:42:02.653966+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  Registro 1600 do Sped Fiscal?
type: support-article
updated_at: '2023-03-08T18:03:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013152511-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-Registro-1600-do-Sped-Fiscal
---

**Dúvida**Como gerar o registro 1600 do SPED FISCAL.  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.   
  
**Solução**Para solucionar a dúvida acima, verifique as orientações:  
Este registro poderá ser tratado via módulo **SIGALOJA** ou por Venda Direta configurando os seguintes campos:  
Tabela **SL4**, campos **L4\_FORMA** = CC ou CD, **L4\_VALOR** e **L4\_ADMINIS**

Módulo **SIGALOJA**  
  
1. Cadastre as Administradoras Financeiras;

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2018%3A5%3A15.png?version=1&modificationDate=1465156762000&api=v2)

**Tipo Adminstr**=CC - para cartão de crédito, ou DB  para cartão de débito.

2. **Rede Destino** = Selecione a empresa administradora – esse campo é responsável para geração do registro 1600 unificado das administradoras financeiras.  
Importante: Ao criar um cadastro na **SAE**, o sistema cria o mesmo na tabela **SA1**, para preencher os dados e gerar o registro **0150** corretamente;  
  
3. Verifique o cadastro de Administradoras (tabela **SAE**), TODOS cadastros devem ser preenchidos corretamente;  
Campos:  
- Tipo Admins (**AE\_TIPO**);  
- Rede Destino (**AE\_REDE**), informe a rede para que o sistema gere corretamente. Caso não exista, efetue o cadastro na tabela genérica **L9** via configurador.

4. Preencher no campo AE\_CODCLI/AE\_LOJCLI com o código do cliente referente a administradora financeira .  
  
5. No cadastro de cliente, TODAS as administradoras devem possuir o cadastro completo:  
Endereço, código de municípios, UF, bairro, CNPJ, inscrição estadual, país, etc;

**![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2018%3A8%3A25.png?version=1&modificationDate=1465156952000&api=v2)**

6. Gere o cupom, no passo do **F7**, clicar na opção Zerar Pagamentos e depois selecionar “Cartão de Crédito”;

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2018%3A9%3A42.png?version=1&modificationDate=1465157029000&api=v2)

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2018%3A9%3A59.png?version=1&modificationDate=1465157046000&api=v2)![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2018%3A10%3A19.png?version=1&modificationDate=1465157067000&api=v2)

**Esta caixa aparece após o F5**O sistema gera as informações na tabela **SL4**, de onde busca os dados para o registro **1600**, de acordo com os dados dos campos selecionados abaixo.

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2018%3A12%3A9.png?version=1&modificationDate=1465157176000&api=v2)

7. Na Wizard do **SPEDFISCAL** deixe a pergunta **Gera Registro de ECF** = 1-Sim;

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2018%3A14%3A21.png?version=1&modificationDate=1465157308000&api=v2)

8. Gere o registro **1600** - **Cartão de Credito /Debito** = 1- Sim;

![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2018%3A15%3A45.png?version=1&modificationDate=1465157392000&api=v2)

**Importante**Caso não tenha módulo **SIGALOJA** ou Venda Direta, deverá ser utilizado a geração do registro **1600** via ponto de entrada **SPDFIS10**

Regra do ponto de entrada para composição do campo **COD\_PART:**

Seguindo a lógica para correta composição do campo **COD\_PART** do registro **1600** via ponto de entrada  - **SA1**+FILIAL+**CODPART**+LOJA  
Tratando da seguinte forma  
**SA1**= irá ocupar 3 caracteres +2 caracteres da FILIAL+6 caracteres do **CODPART**+2 caracteres da LOJA, Totalizando = 13 caracteres  
  
Caso o código do participante não tenha 6 caracteres, deve ser utilizadas as 6 posições deixando os demais campos em branco.

Ponto de entrada **SPDFIS10** do tratamento no ponto de entrada.

aAdd (aReg1600, {"99","SA101002 01","ADMIN FINANC VISA\_1",100,100})//.  
Link: <http://tdn.totvs.com/pages/releaseview.action?pageId=6077182>
