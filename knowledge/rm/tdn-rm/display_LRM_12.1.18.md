---
content_hash: 663fa869ca18b6804c227dd45f52daebb9b35fbf95e63fb80ca91df2aa430b0d
fetched_at: '2026-06-29T00:09:23.175290+00:00'
page_id: '422546061'
product: rm
source: tdn-rm
title: 12.1.18
type: documentation
url: https://tdn.totvs.com/display/LRM/12.1.18
version: 8
---

* O registro [N600](http://tdn.totvs.com/pages/viewpage.action?pageId=422545978) da ECF foi ajustado para comportar os cálculos de valores de acordo com o código da tabela dinâmica e efetuar a soma corretamente.
* Melhoria na geração da
* **Tela de Geração do** [SPED FISCAL](http://tdn.totvs.com/display/LRM/Gerar+SPED+FISCAL)**:** Criada nova aba "Dados do Inventário" na tela de geração do SPED Fiscal com campos pertinentes a geração do bloco H e adicionado nela novo campo "Motivo do Inventário 2" com mesmas opções e validações do campo "Motivo do Inventário".
* **Alterações cadastrais para a implementação da** [EFD Reinf](http://tdn.totvs.com/display/LRM/EFD-REINF)

2
incomplete
[Cadastro de Processos Judiciais e Administrativos](http://tdn.totvs.com/display/LRM/Processo+Judicial+e+Administrativo)

Tipo de Processo com as opções : Administrativo, Judicial  
 UF da Seção Judiciária  
 Flag para informar se o autor da ação é terceiro  
 Cliente/Fornecedor quando o processo não for da própria empresa. Este campo é obrigatório se o flag "Autor da Ação é Terceiro" estiver marcado.  
 Em atendimento à geração da EFD Reinf foi criado o anexo de Tributos Discutidos para associar o(s) Tributo(s) aos quais o processo se relaciona. Para cada Processo poderão ser incluídos tantos tributos forem necessários.  
 Implementado o log das alterações no cadastro de processos Judiciais. Neste log serão armazenadas as alterações feitas nos campos: Tipo de Processo, Número do Processo, UF da Seção Judiciária, Município da seção judiciária e Autoria da Ação.  
 Implementado o log das alterações no cadastro de Tributos Discutidos dos Processos Judiciais que irá armazenas as alterações feitas nos campos: Indicativo da Suspensão, Data da Decisão, Depósito do montante integral.

3
incomplete
[Log de alterações no Cadastro de Filiais](http://tdn.totvs.com/display/LRM/Log+de+Filial)

Incluídos no log de alterações os campos abaixo.  
    
 **Aba Tipo de Estabelecimento**  
   Classificação Tributária  
   Filial é Órgão Publico  
   CNPJ do Ente Federativo Responsável  
    
 **Aba Dados Adicionais**  
   Desoneração da Folha CPRB  
   Acordo Inter. Isenção de Multa  
   Empresa Obrigada (ECD)  
    
 **Aba Contador**  
  Nome do Contador  
  CPF/CNPJ Contador  
  DDD e Telefone do Contador  
  DDD e Celular do Contador  
  e-mail do Contador

4
incomplete
[Dados Fiscais do Produto](http://tdn.totvs.com/pages/viewpage.action?pageId=423938199)

Implementado o campo de Classificação do Serviço onde deve ser informado o código de classificação do serviço prestado mediante cessão de mão de obra/empreitada sujeito a retenção de Contribuição Previdenciária de acordo com a Tabela 06 da Reinf.

* Implementado o campo Código Classificação Econômica onde deve ser informado o Código de Atividades, Produtos e Serviços sujeitos a Contribuição sobre a Receita Bruta, conforme Tabela 09 da Reinf.
* [Cadastro de INSS - PJ](http://tdn.totvs.com/pages/viewpage.action?pageId=423937960): Criados os campos abaixo no cadastro de INSS do TOTVS Gestão de Estoque, Compras e Faturamento para atender à geração da Reinf:

  5
  incomplete
  Alíquota Adicional 15 anos

  6
  incomplete
  Alíquota Adicional 20 anos

  7
  incomplete
  Alíquota Adicional 25 anos

  8
  incomplete
  Alíquota GILRAT

  9
  incomplete
  Alíquota SENAR

  10
  incomplete
  Código da Receita FUNRURAL

  11
  incomplete
  Código da Receita SENAR

* Implementado o [Cadastro de Certificados Digitais](http://tdn.totvs.com/display/LRM/Certificado+Digital)
* [Apuração e Geração de DARF IRRF-PJ](http://tdn.totvs.com/pages/viewpage.action?pageId=422545899) - A apuração e geração de DARF para este tributo passou a considerar o parâmetro de geração do tributo IRRF-PJ gravado no TOTVS Gestão Financeira.
* [Cadastro Exercício](http://tdn.totvs.com/pages/viewpage.action?pageId=422545699): Foi feito um ajuste neste cadastro para que o campo "Mascara do Código de Natureza" possa receber apenas "#" - Isso significa que no Cadastro de Natureza o campo Código da Natureza vai receber apenas números.
* [Geração do registro F525 por documentos agrupados por CST - Código da Situação Tributária](http://tdn.totvs.com/pages/viewpage.action?pageId=422545734).
* [Melhoria na geração dos registros 0450\E340 - Livro Eletrônico - Ato Cotepe](http://tdn.totvs.com/pages/viewpage.action?pageId=422545912).
* Melhoria na geração da Rotina Estadual [GIA SP](http://tdn.totvs.com/pages/viewpage.action?pageId=422545622), para que não seja considerado o valor do IPI como outros impostos quando o tributo estiver parametrizado como não tributado e afeta base de cálculo do ICMS.
* Incluído nos Lançamentos fiscais os Tipos Fretes "Próprio Remetente" e "Próprio Destinatário" na rotina [DIA Amazonas](http://tdn.totvs.com/pages/viewpage.action?pageId=422546023).
* Alteração na geração do campo "Número de Inscrição da obra", na rotinas [RMD](http://tdn.totvs.com/pages/viewpage.action?pageId=422546141).
* Implementado o processo de [Cancelamento da NFS-e](http://tdn.totvs.com/display/LRM/Cancelar+NFS-e) e Movimento quando o município não disponibiliza integração eletrônica para o cancelamento da NFS-e.
* [Implementação do Município de Indaiatuba - SP - DESISS (txt)](http://tdn.totvs.com/pages/releaseview.action?pageId=64651845).
* DIME – SC: Criado um novo [Subtipo "Crédito relativo Substituição Tributária](http://tdn.totvs.com/pages/viewpage.action?pageId=422545651)", no Lançamentos de Outros Débitos\Créditos para atendimento da legislação.
