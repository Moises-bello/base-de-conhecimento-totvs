---
content_hash: 25b9c9a71259c272027b271fb22e94ed6ee7c0ef2c6ba7828d637873ff19331e
fetched_at: '2026-06-29T00:09:47.087286+00:00'
page_id: '435104915'
product: rm
source: tdn-rm
title: Empreendimento - Integração - EFD - PIS/Cofins
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104915
version: 13
---

Para a correta geração das informações da atividade imobiliária os empreendimentos/unidades vendidas deverão ter seus cadastros completos com todas as informações relevantes para a sua correta identificação de acordo com especificação do TOTVS Incorporação.  
Além dos dados de identificação do  e unidades, os dados a seguir também deverão ser informados.

* Acesse o menu Cadastros | Manutenção de empreendimentos | Empreendimento | Selecione e edite o empreendimento desejado | Acesse a aba EFD-PIS/Cofins.

É necessário preencher os campos para a correta geração do registro.

* Acesse o menu Cadastros | Manutenção de empreendimentos | Bloco / Apto | Anexos | Apto | Pode-se selecionar uma ou mais subunidades | Processos | Atualizar em Lote | Na tela de 'Endereço' existe a opção para atualizar os dados do PIS/COFINS.
* Utilizar data de compensação ao invés de data da baixa: Com essa opção marcada o sistema irá sempre considerar o período da data de compensação do extrato de caixa.
* Gerar registro 1800 da EFD independentemente da data de habite-se: Informa se o registro 1800 deve ser gerado independentemente da data de comercialização da venda. Tanto para os imóveis não entregues (como está hoje), quanto para os já entregues, ou seja, os valores referentes a imóveis já entregues, com data de habite-se preenchida, também deverão ser enviados para o registro 1800 da EFD.

Após finalizar este processo o sistema está apto a gerar os registros F200, F210 e F205.  
Este processo deve ser feito todo mês antes da geração dos registros da EFD PIS/COFINS.  
A execução do processo de EFD Contribuições é feita pelo módulo Fiscal do RM. O arquivo é gerado na pasta Saídas dentro da pasta RM.Net e paralelamente é gerado um log dos cálculos realizados para a geração dos valores no F200. Este log dos valores calculados é gerado dentro da pasta LOG\_SPED que também fica dentro da pasta RM.Net.

* [Atividades Imobiliárias](http://tdn.totvs.com/pages/viewpage.action?pageId=422545902)

VERSÃO 12.1.2209 em diante!!

**Somente 12.1.2602 . Foi criado um novo parâmetro UsaRet na abar sped , isso porque um mesmo empreendimento que é comercial e residencial , um pode ser F200  e outro Ret 1800, com essa nova parametrização é possível um mesmo CNPJ de empreendimento ter configurações diferentes.**

Foi criado um parâmetro para tratar o registro 1800 da EFD independentemente da data de habite-se do empreendimento.  
Ele informa se o registro 1800 deverá ser gerado independentemente da data de comercialização da venda, ou seja, os valores referentes a imóveis já entregues, com data de habite-se preenchida, também serão enviados.   
Caso esse parâmetro esteja habilitado, tanto para os imóveis não entregues (como está hoje), quanto para os já entregues, o valor deverá ser enviado para o registro 1800 da EFD.

**Como fazer:**

Para geração do RET 1800, é necessário acessar  o menu Cadastro | Básicos | Filiais | Edita a filial desejada | Anexos | Dados Fiscais | Tributos | Deve-se marcar a *flag* "Apura pelo Regime Especial Tributação".

Ou se preferir por ser feito também acessando Cadastro | Empreendimento | Editar | Integração | Gestão Financeira | Filial | Edita a Filial | Anexos | Dados Fiscais | Tributos | Deve-se marcar a *flag* "Apura pelo Regime Especial Tributação".

Verifique se existe na tela tributos a tributação do tipo RET conforme a imagem abaixo, caso não tenha, favor registrar esse tributo.  
  
  
  
favor verificar e seguir os passos desses dois links abaixo caso queira mais detalhes sobre o cadastro e parametrização do tributo do tipo RET : 

Esse primeiro link ajuda a criar os períodos de cada tipo de tributação, caso não tenha.

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024406792-Cross-Segmentos-Linha-RM-FIS-Inserir-M%C3%BAltiplos-Per%C3%ADodos>

Essa documentação ensina de forma detalhada toda a parametrização do tipo RET.  
<https://tdn.totvs.com/pages/releaseview.action?pageId=320378257>
