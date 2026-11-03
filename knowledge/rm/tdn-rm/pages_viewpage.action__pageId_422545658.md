---
content_hash: 90373f0a8a736e2d8afb12cfa926e303b1305dcb5ae505cff7225f1d09b0c60b
fetched_at: '2026-06-29T00:09:20.092964+00:00'
page_id: '422545658'
product: rm
source: tdn-rm
title: Outros Tributos (INSS/FUNRURAL)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545658
version: 6
---

Para atendimento da obrigação acessória Escrituração Fiscal Digital das Retenções e Informações da Contribuição Previdenciária Substituída – EFD Reinf, foram criados os seguintes campos para os tributos INSS e FUNRURAL:

**Identificação**

**Base**: A base dos tributos INSS e FUNRURAL será calculado da seguinte forma:  
Valor Bruto dos Serviços  Deduções de Material/Equipamento  Deduções Alimentação  Dedução de Transporte

**Valor**: Será o resultado da seguinte fórmula:  
Valor da Retenção  Valor retido subcontratados  Retenção Suspensa/Depósito Judicial  Retenções Adicionais 15, 20 e 25 anos  Retenção Adicional Suspensa/Depósito Judicial  Valor da Contribuição GILRAT  Valor da Contribuição SENAR  
***Observação***: Não será possível editar ambos os campos para os tributos INSS e FUNRURAL.

**Identificador INSS/PJ**: Informado de acordo com a obrigatoriedade. Este campo é referente a um Identificador existente no Cadastro INSS/PJ, utilizado no processo de Geração de Guias Automaticamente no Período de Apuração.

Esse código será carregado automaticamente em Outros Tributos do item caso exista a informação no cadastro do INSS/PJ vinculado ao Cliente\Fornecedor ou no cadastro do Tributo.

**Memória de Cálculo**

**Valor Bruto dos Serviços**: Ao selecionar os tributos INSS ou FUNRURAL o sistema irá preencher default com o Valor da Mercadoria do item do lançamento.

**Deduções de Materiais/Equipamentos, Alimentação e Transporte**: Deverá ser informado manualmente pelo usuário.

**Base de Cálculo da Retenção**: Será calculado da seguinte forma:  
Valor Bruto dos Serviços  Dedução de Material/Equipamento  Dedução de Alimentação  Dedução de Transporte

**Alíquota:** Preenchido com o Código de Receita do INSS cadastrado no anexo [Defaults do Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388823) | Outros Dados selecionado do Cli/For selecionado no Lançamento Fiscal. Caso a alíquota não seja informada no cadastro do Código de Receita ou não exista nenhum vinculo no cadastro do [Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388786), será preenchido com a alíquota informada no cadastro do [Tributo](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546150).

**Valor da Retenção:** Campo não editável, preenchido com o cálculo Base de Cálculo da Retenção  Alíquota.

**Valor retido subcontratados:** Habilitado apenas para o tributo INSS que poderá ser preenchido pelo usuário.

**Retenção Suspensa/Dep. Jud.:** Campo não obrigatório que poderá ser informado pelo usuário.

**Serviços Especiais**

Aba visível apenas quando selecionado o tributo **INSS.**

**Valor do Serviço 15 anos de contribuição**: Campo preenchido pelo usuário.

**Valor do Serviço 20 anos de contribuição**: Campo preenchido pelo usuário.

**Valor do Serviço 25 anos de contribuição**: Campo preenchido pelo usuário.

**Alíquota 15 anos de contribuição**: Preenchido com o Código de Receita do INSS (campo Alíquota adicional - 15 anos), cadastrado no anexo [Defaults do Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388823) | Outros Dados selecionado do Cli/For selecionado no Lançamento Fiscal. Caso a alíquota não seja informada no cadastro do Código de Receita ou não exista nenhum vinculo no cadastro do [Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388786), será preenchido com a alíquota informada no cadastro do [Tributo](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546150).

**Alíquota 20 anos de contribuição**: Preenchido com o Código de Receita do INSS (campo Alíquota adicional - 20 anos), cadastrado no anexo [Defaults do Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388823) | Outros Dados selecionado do Cli/For selecionado no Lançamento Fiscal. Caso a alíquota não seja informada no cadastro do Código de Receita ou não exista nenhum vinculo no cadastro do [Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388786), será preenchido com a alíquota informada no cadastro do [Tributo](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546150).

**Alíquota 25 anos de contribuição**: Preenchido com o Código de Receita do INSS (campo Alíquota adicional - 25 anos), cadastrado no anexo [Defaults do Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388823) | Outros Dados selecionado do Cli/For selecionado no Lançamento Fiscal. Caso a alíquota não seja informada no cadastro do Código de Receita ou não exista nenhum vinculo no cadastro do [Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388786), será preenchido com a alíquota informada no cadastro do [Tributo](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546150).

**Valor da Retenção 15 anos de contribuição**: Preenchido com o resultado do calculo dos campos Valor 15 anos de contribuição  Alíquota 15 anos de contribuição.

**Valor da Retenção 20 anos de contribuição**: Preenchido com o resultado do calculo dos campos Valor 15 anos de contribuição  Alíquota 20 anos de contribuição.

**Valor da Retenção 25 anos de contribuição**: Preenchido com o resultado do calculo dos campos Valor 15 anos de contribuição  Alíquota 25 anos de contribuição.

**Retenção adicional susp/dep. jud**: Campo preenchido pelo usuário.

**GILRAT/SENAR**

Aba visível apenas quando selecionado o tributo **FUNRURAL.**

**Alíquota GILRAT**: Preenchido com o Código de Receita do INSS (campo "Alíquota GILRAT"), cadastrado no anexo [Defaults do Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388823) | Outros Dados selecionado do Cli/For selecionado no Lançamento Fiscal. Caso a alíquota não seja informada no cadastro do Código de Receita ou não exista nenhum vinculo no cadastro do [Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388786), será preenchido com a alíquota informada no cadastro do [Tributo](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546150).

**Alíquota SENAR**: Preenchido com o Código de Receita do INSS (campo "Alíquota SENAR"), cadastrado no anexo [Defaults do Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388823) | Outros Dados selecionado do Cli/For selecionado no Lançamento Fiscal. Caso a alíquota não seja informada no cadastro do Código de Receita ou não exista nenhum vinculo no cadastro do [Cliente/Fornecedor](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388786), será preenchido com a alíquota informada no cadastro do [Tributo](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546150).

**Valor da Contribuição GILRAT**: Campo editável porém calculado B. de Cálculo da Retenção  Alíquota GILRAT.

**Valor da Contribuição SENAR**: Campo editável porém calculado B. de Cálculo da Retenção  Alíquota SENAR.

**Valor NÃO Retido GILRAT**: Campo preenchido pelo usuário.

**Valor NÃO Retido SENAR**: Campo preenchido pelo usuário.

**Tributos Defaults da Natureza**

Os tributos INSS ou Funrural que estiverem parametrizados como Defaults na Natureza de Operação (Cadastro da Natureza > Anexos > Tributos da Natureza) vão ser carregados automaticamente no item do Lançamento Fiscal, seguindo a mesma regra do preenchimento manual onde os dados são carregados a partir do cadastro do INSS vinculado ao Cliente\Fornecedor do lançamento, caso não exista essa informação no Cliente\Fornecedor será verificado no cadastro do tributo.

ATENÇÃO

**A geração das guias passou a considerar estes tributos quando estão informados nos itens do Lançamento Fiscal.**   
**Apesar da carga dos valores para a geração da guia de recolhimento ainda ser feita no Lançamento Fiscal quando estes não constarem nos itens aconselhamos a gravação destas informações sempre nos itens do lançamento e somente lá para evitar duplicidade de valores.**
