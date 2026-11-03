---
content_hash: 2e514bd0658040b53cabdaef72c2a11097c251e52fa28a9de1c260e487969da5
fetched_at: '2026-06-29T00:10:06.641663+00:00'
page_id: '452719324'
product: rm
source: tdn-rm
title: Seções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719324
version: 25
---

Seções de uma empresa são partições onde serão feitas as alocações de pessoal.  
   
Para a utilização do cadastro de seções na folha de pagamento é importante que seja cadastrada uma filial distinta para cada CNPJ nos Cadastros Globais de Filiais, e em seguida, todos os departamentos cadastrados relacionados a esta filial nos Cadastros Globais de Departamentos.  
   
No  Parametrizador máscaras e quebras determine a Máscara Código de Seção, Código de quebra mestre, o Código de quebra para CNPJ ou CEI, que o módulo utilizará para o cadastro da hierarquia do código de seções.   
   
**Atenção:**  
Para qualquer ícone desabilitado, verifique com o Supervisor as permissões do usuário em questão, no módulo de Serviços Globais em Perfis na pasta Acesso a Menus.  
   
O código da seção deve respeitar a Máscara de Código de Seção. A hierarquia do cadastro de seção deve respeitar o Código de quebra mestre, Código de quebra para CNPJ ou CEI, definidos No parametrizador em RH – Máscaras e Quebras.  
   
**Exemplo:**   
**CNPJ**  
Há os seguintes Códigos cadastrados:  
0 Empresa Exemplo 24.867.387/ 0001-38 01 Emp. Exemplo - Matriz 24.867.387/ 0001-38 01.01 DST - Depto. Suporte Técnico 24.867.387/ 0001-38 01.02 COM - Depto. Comercial 24.867.387/ 0001-38 02 Emp. Exemplo - Filial RJ 24.867.387/ 0002-23 02.01 DST - Depto. Suporte Técnico 24.867.387/ 0002-23 02.02 COM - Depto. Comercial 24.867.387/ 0002-23

* + Se for incluída uma seção com o código "01.03", automaticamente o campo CNPJ será preenchido com o número "24.867.387/0001 - 38", pois o código informado pertence à quebra "01" (centralizadora).
  + Se for incluída uma seção com o código "02.01.01", automaticamente o campo CNPJ será preenchido com o número "24.387.867/ 0001 - 23", pois o código informado pertence à quebra "02" (centralizadora).
  + Se for incluída uma seção com o código "1", automaticamente o campo será preenchido com o número "24.387.867" (sem o controle 000x-xx), porque não há uma quebra centralizadora para este novo código.

Cód. na CEF é o código é fornecido pela CEF e será utilizado para a geração do SEFIP.   
   
O módulo de Folha de Pagamento trata como "filial" todas as unidades de uma coligada. Portanto, a matriz também deve constar no cadastro de "filiais".  
   
**Observações:**

1. Se o parâmetro "Número da ficha de registro gerada pelo sistema" que está no parametrizador estiver desmarcado, não será permitido trocar a filial da seção porque o número da ficha de registro do funcionário é informado pelo usuário e não será gerenciado automaticamente pelo sistema. Assim, não ocorrerá duplicidade no número da ficha de registro de empregados em um mesmo CNPJ, o que não é permitido pelo sistema.
2. Se o parâmetro "Número da ficha de registro gerada pelo sistema" que está no parametrizador estiver marcado, será permitido trocar a filial da seção porque o número da ficha de registro do funcionário é gerenciado automaticamente pelo sistema em ordem sequencial. Assim, não ocorrerá duplicidade no número da ficha de registro de empregados em um mesmo CNPJ, o que não é permitido pelo sistema.
3. Se os parâmetros "Número da ficha de registro gerada pelo sistema" e "Numeração específica para cada CNPJ" que está no parametrizador estiverem marcados, será permitido trocar o código da seção SOMENTE para o mesmo CNPJ porque o número da ficha de registro do funcionário é gerenciado automaticamente pelo sistema e com numeração específica para cada CNPJ. Assim, não ocorrerá duplicidade do número da ficha de registro de empregados para outro CNPJ, o que não é permitido pelo sistema.

A informação de Calendário é útil em caso de seções instaladas em localidades diferentes, podendo não haver coincidência de feriados.   
   
O tipo de lotação deve ser preenchido com o código relacionado ao e-Social (S1020).    
**Observação:**  
Sempre que a empresa for identificada por CPF, ou seja, marcada como Pessoa Física deverá ter um CEI vinculado para o recolhimento correto da GPS. Veja parametrização no parametrizador em RH – Máscaras e Quebras.  
   
**Atenção:**  
Legislação Específica - Instrução Normativa Nº 071 de 10/05/2002.  
   
 CAEPF - Preencher com o Número da atividade econômica de pessoa física. Este campo será habilitado somente quando o campo pessoa física estiver marcado   
   
 Tipo CAEPF -   Informe o tipo conforme layout do eSocial. Preenchimento obrigatório para a geração do XML S1005   
   
O campo Pessoa Física alterará a correspondência entre os Códigos de vínculo cadastrados no Folha de Pagamento e a tabela de vínculos da RAIS.  
   
**Exemplos:**

1. Vínculo do funcionário no Folha de Pagamento igual a 1 (contrato de trabalho expresso ou tácito pela CLT):
   * Campo "Pessoa Física" marcado
     + Será impresso na RAIS o código 15 (trabalhador urbano vinculado a empregador pessoa física por contrato de trabalho regido pela CLT, por prazo determinado).
   * Campo "Pessoa Física" desmarcado
     + Será impresso o código 10 (trabalhador urbano vinculado a empregador pessoa jurídica).
2. Vínculo do funcionário no Folha de Pagamento igual a 6 (trabalhador rural):
   * Campo "Pessoa Física" marcado
     + Será impresso na RAIS o código 25 (trabalhador rural vinculado a empregador pessoa física por contrato de trabalho regido pela CLT, por prazo indeterminado)
   * Campo "Pessoa Física" desmarcado
     + Será impresso o código 20 (trabalhador rural vinculado a empregador pessoa jurídica).

O parâmetro Identificação pelo CNPJ define se o estabelecimento é identificado pelo CNPJ ou pelo CEI.  
   
Os campos de Controle de Lotação ficarão desabilitados para controle do limite de vagas pelo módulo de Gestão de Pessoas. Caso o controle seja cadastrado será demonstrado na pasta de identificação da seção.  
   
Caso não haja integração entre os módulos de folha de pagamento e gestão de pessoas, o controle de lotação poderá ser feito marcando no parametrizador da folha de pagamento o parâmetro "Usa controle de Limite de Funcionários por Seção" em Integrações no item Gestão de Pessoas.  
   
Informe no limite o número de funcionários que será permitido na seção.   
   
Para as bases que o campo "**Usa controle de Limite de Funcionários por Seção**" no parametrizador estiver marcado e o campo "**Limite de Funcionários**" estiver com valor zero, será apresentada, em casos de inclusão e transferência de funcionários, a mensagem "**Limite de funcionários para esta seção já foi esgotado**".  
   
Se estiver com um determinado valor, será permitida a inclusão de um número de funcionários menor ou igual ao limite definido.   
   
Se o campo "**Usa controle de Limite de Funcionários por Seção"** no parametrizador estiver desmarcado, o campo "Limite" será visualizado com o status de "**Sem Controle**" e poderá ser admitido funcionários sem controle de lotação.  
   
No campo Alocadas será exibida a quantidade de funcionários que estão cadastrados nesta seção.  
   
No campo Disponíveis será exibida a quantidade de vagas disponíveis para esta seção.   
   
Este campo somente terá valor diferente de 0 (zero) quando o campo "Usa controle de Limite de Funcionários por Seção" no parametrizador estiver marcado ou a empresa que possui o módulo de Gestão de Pessoas estiver utilizando o Controle de Lotação do   
Gestão de Pessoas na pasta Controle de Lotação do parametrizador.   
   
No campo Excedentes será exibida a quantidade de funcionários que foram admitidos e estão excedendo a quantidade de vagas.   
   
O campo Excedentes somente terá valor diferente de 0(zero) quando o campo "Permite incluir acima do limite na Seção" no parametrizador estiver marcado ou a empresa que possui Gestão de Pessoas estiver utilizando o Controle de Lotação com o parâmetro "Permite Admissões Acima do Limite" marcado na pasta Controle de Lotação do parametrizador.  
   
Os campos do Grupo Verbas: "Limite", "Alocadas", "Disponíveis" e "Excedentes" de Verbas não são para controle do módulo Folha de Pagamento. Estes campos são informativos referentes aos clientes que possuem integração entre os módulos Folha de Pagamento e Gestão de Pessoas e usam este controle interno disponível somente para o módulo Gestão de Pessoa. No momento de inclusão de funcionários, será validado de acordo com a parametrização do módulo Gestão de Pessoas.  
   
**Atenção I:**

* Para atender a Nota de Documentação Evolutiva **'NDE 01/2018 - Eventos de Segurança e Saúde no Trabalho - SST'** liberada pela receita federal no dia 30/05/2018, foi criado no cadastro de seções, o anexo "Informações sobre Segurança e Saúde no Trabalho (SST)", para inclusão das informações dos programas de SST de cada seção. Esse anexo é alimentado pela tabela dinâmica VPROGDOC (Tabela 30: Programas, Planos e Documentos).   
  Para habilitar esse novo anexo, é necessário liberar o acesso nos perfis referentes ao módulo Folha de Pagamento ou então ao módulo Segurança e Saúde Ocupacional.

**Observação:** Essas informações devem ser lançadas nas seções centralizadoras de CNPJ, visto que estes registros são os válidos para o evento S-1005 do eSocial.

**Atenção II:**

* Para atender ao FUNRURAL lei 13.606/91, foi criado no cadastro de seções, o anexo **Histórico de Percentuais para INSS**.
* Para habilitar o anexo deverá ir no Parametrizador | Folha mensal | Encargos Sociais  e selecionar o parâmetro:  ["Habilita Histórico de INSS no Cadastro de Seção"](http://tdn.totvs.com.br/pages/releaseview.action?pageId=490324995)

**Pastas da Seção**

[Endereço - Fop](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719876)

Dados Contábeis

Dados p/ INSS

RAIS / CAGED/eSocial

eSocial

Descrição do Local

Descrição do Ambiente de Trabalho

Vale Refeição

Vale Transporte

nte

Funcionários Lotados

Contribuição Sindical

`V`

Funcionários Lotados

---

Trocar Código da Seção
