---
content_hash: 857fb4cf2d267453a4e40c00647f82fb3f23fa6892fe88a439b39b1f672d040d
fetched_at: '2026-06-29T00:10:38.790264+00:00'
page_id: '544732520'
product: rm
source: tdn-rm
title: Middleware - Como gerar no S-1200 a tag <ideDmDev> com prefixo para múltiplos
  vínculos na mesma coligada?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544732520
version: 14
---

false

**A partir das Versões:**

* 12.1.26.206
* 12.1.27.155
* 12.1.28.000

# Objetivo:

---

Detalhar maneiras para a geração da tag <ideDmDev> do evento S-1200, utilizando prefixo para múltiplos vínculos na mesma coligada.

FIQUE ATENTO!

Os autônomos fluxus/externos serão apresentados na fila de eventos pelo seus respectivos CPF's.

1true1Execução do scriptExecução do script

Para a criação do campo será necessário atualizar a base no sistema RM.Atualizador.exe.

2Múltiplos Vínculos FluxusMúltiplos Vínculos Fluxus

No exemplo abaixo, existem dois cadastros de autônomos com o mesmos CPF, sendo que um deles possui o cadastro do prefixo:

Código: A12345 e código de categoria: 712

Código: F12345 e código de categoria: 701

Acessar o menu Backoffice | Gestão Financeira | Cadastros | Clientes Fornecedores | Anexos | eSocial

1) Preencher o campo "Prefixo Período" para o cliente/fornecedor (código "F12345" e código de categoria "701").

**Observações:**

* O campo poderá ser preenchido com números e/ou letras.
* O valor preenchido neste campo será concatenado na tag <ideDmDev>, impedindo assim que ocorra duplicidade de períodos.

2) Realizar o lançamento financeiro para os dois vínculos, sendo que:

Para o cliente/fornecedor com o código "A12345" (sem o cadastro de prefixo), o lançamento foi realizado na data 15/07/2019.

Para o cliente/fornecedor com o código "F12345" (com o cadastro de prefixo), o lançamento foi realizado na data 05/07/2019.

Após cadastrar essas informações, deverá gerar o xml do evento S-1200 (RH | Folha de Pagamento | eSocial | Gerar XML), conforme demonstrado abaixo:

**observação :** Com a utilização do Middleware não há necessidade de marcação do parâmetro **Gerar Autônomos FluxusExternos** para geração do XML dos autônomos do FLuxus/ Externos. Por isso, o parâmetro foi removido da tela.

O sistema irá gerar o xml unificado para os autônomos, com os lançamentos acima, sendo:

* Para o cliente/fornecedor código "A12345" (sem o cadastro do prefixo) será gerada na tag <ideDmDev> o valor padrão 1.
* Para o cliente/fornecedor código "F12345" (com o cadastro do prefixo) será gerada na tag <ideDmDev> o valor 1A (número padrão 1 + A) .

3Funcionário e outro Vínculo Autônomo ExternoFuncionário e outro Vínculo Autônomo Externo

1. Acessar o cadastro do funcionário que possui vinculo, pasta "Parâmetros";
2. Preencher o campo "Prefixo Período (eSocial)" de acordo com a necessidade;

**Observação:** O valor preenchido neste campo será concatenado na tag <ideDmDev>, impedindo assim que ocorra duplicidade de períodos.

1. Salvar as alterações.
2. O envelope de pagamento abaixo foi lançado no período 1.

3. No menu Encargos | Autônomos Externos, existem informações importadas para o mesmo CPF da chapa acima.

Após cadastrar essas informações, deverá gerar o xml do evento S-1200 (RH | Folha de Pagamento | eSocial | Gerar XML), conforme demonstrado abaixo:

**observação :** Com a utilização do Middleware não há necessidade de marcação do parâmetro **Gerar Autônomos FluxusExternos** para geração do XML dos autônomos do FLuxus/ Externos. Por isso, o parâmetro foi removido da tela.

O sistema irá gerar o xml unificado para o funcionário e autônomo, acrescentado o prefixo "F" cadastrado no funcionário conforme demonstrado acima.

Será gerado na tag <ideDmDev> o valor 1F (número período lançado + F) .

**Observação**: Para a folha de pagamento do autônomo externo, a tag <ideDmDev> será calculada com o valor fixo 1.

4Funcionário e outro Vínculo Autônomo FluxusFuncionário e outro Vínculo Autônomo Fluxus

1. Acessar o cadastro do funcionário que possui vinculo, pasta "Parâmetros".
2. Preencher o campo "Prefixo Período (eSocial)" de acordo com a necessidade.

**Observação:** O valor preenchido neste campo será concatenado na tag <ideDmDev>, impedindo assim que ocorra duplicidade de períodos.

1. Salvar as alterações.
2. O envelope de pagamento abaixo foi lançado no período 1.

Acessar o menu Backoffice | Gestão Financeira | Cadastros | Clientes Fornecedores | Anexos | eSocial e preencher o campo "Prefixo Período" para o cliente/fornecedor (código "C00012" e código de categoria "701").

2) Realizar o lançamento financeiro.

Neste exemplo o lançamento foi na data 18/07/2019 para o cliente/fornecedor com o código "C00012".

Após cadastrar essas informações, deverá gerar o xml do evento S-1200 (RH | Folha de Pagamento | eSocial | Gerar XML), conforme demonstrado abaixo:

**observação :** Com a utilização do Middleware não há necessidade de marcação do parâmetro **Gerar Autônomos FluxusExternos** para geração do XML dos autônomos do FLuxus/ Externos. Por isso, o parâmetro foi removido da tela.

O sistema irá gerar o xml unificado para o funcionário e autônomo, com os lançamentos acima, sendo que:

* Para o funcionário (com prefixo F) será gerada na tag <ideDmDev> o valor 1F (número período lançado + F).
* Para o cliente/fornecedor código "C00012" (com prefixo C) será gerada na tag <ideDmDev> o valor 1C (número padrão 1 + C) .
