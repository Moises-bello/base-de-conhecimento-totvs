---
content_hash: 0b67262b87a99b72afb17b6d9ecb779e0f112d2516508f9fb9dbf565a5c26263
fetched_at: '2026-06-29T00:09:27.917908+00:00'
page_id: '423938569'
product: rm
source: tdn-rm
title: Gerar SPED FCONT
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerar+SPED+FCONT
version: 4
---

Para gerar o **SPED FCONT** alguns procedimentos devem ser efetuados previamente no RM Saldus, outros diretamente no Programa Validador da Entrada de Dados do FCONT (PVA – FCONT) liberado pela Receita Federal. Abaixo seguem os passos:

**1º passo**   
Verificar se todos os lançamentos contábeis do ano que se deseja enviar já estão devidamente cadastrados no sistema, e se o resultado do período já foi apurado (Lucro ou Prejuízo). No RM Saldus o resultado do período (Lucro ou Prejuízo) é apurado através do menu Lançamentos | Transferência de Grupos Contábeis. Portanto para gerar o FCONT esta rotina já deve ter sido executada. Lembrando que se deve utilizar um histórico de fechamento para cada ano de encerramento.

**2º Passo:**  
Acessar o plano de contas contábil no menu Cadastro | Plano de Contas Contábil e preencher o campo 'Natureza da conta para emissão do SPED' das contas contábeis.

**3º Passo:**   
Vincular as contas contábeis ao plano referencial da Receita Federal. Esta associação é feita pelo menu Cadastro | Plano de Contas Paralelo. Deve-se selecionar o plano de contas da Receita e clicar na opção 'Anexos | Contas Paralelas', realizar um filtro para apresentar todas as contas referenciais, depois editar a conta referencial e realizar a associação com a conta contábil e se necessário com o centro de custo ou conta gerencial.

**4º Passo:**  
Cadastrar na base de dados um Campo Complementar de Lançamento com o nome 'SPEDFCONT' (Alfanumérico com tamanho = 10).

**5º Passo:**  
Identificar os lançamentos já existentes na base de dados e que deverão ser expurgados para remover os reflexos das alterações introduzidas pela Lei nº 11.638/07, selecionando-os, utilizando a Multi Seleção de Lançamentos e em seguida classificá-los como 'Normal' (lançamentos que no FCONT serão expurgados), através do ícone da visão 'Atualizar o campo complementar SPEDFCONT'. Desta forma, em todos os lançamentos selecionados para esta ação, o campo complementar de lançamento 'SPEDFCONT' será preenchido automaticamente com a letra N.

**Observação**  
Se o parâmetro do sistema 'Usa amarração c.complementar' estiver marcado, ficarão disponíveis na tela de lançamentos, somente os campos complementares de lançamentos que tiverem sido associados às contas contábeis, então, para que o campo complementar 'SPEDFCONT' fique disponível na tela de lançamentos, ele, como qualquer outro campo complementar de lançamento, deverá ser associado às contas contábeis utilizadas nos lançamentos a serem identificados para o SPED.   
Se o parâmetro do sistema 'Usa amarração c.complementar' estiver desmarcado, todos os campos complementares de lançamentos ficam automaticamente disponíveis na tela dos lançamentos, sem que haja necessidade de associá-los às contas contábeis.

**6º Passo:**  
Incluir na base de dados os novos lançamentos com efeito Fiscal (lançamentos de ajustes) e repetir o passo anterior, classificando-os como 'Fiscal'.

**Observação**   
Se desejar não poluir a base de dados com lançamentos que terão somente efeito Fiscal, estes poderão ser incluídos diretamente no PVA, mas caso queira deixar registrado na base estes lançamentos, sugerimos utilizar um Histórico de Fechamento unicamente para este fim, para que seja possível a emissão dos relatórios e apurações desconsiderando estes lançamentos.

**7º Passo:**  
Gerar o arquivo digital, através do Menu Rotinas Legais | SPED Contábil | Gerar SPED FCONT:

* Plano Referencial: esta informação é obrigatória, a não indicação do Plano Referencial irá gerar 'erros' na validação da escrituração no programa validador do FCONT. O Registro I051, Plano de Contas Referencial, é obrigatório, exceto para as pessoas jurídicas que utilizam o plano de contas regulamentado pela SUSEP (campo 02 - QUALI\_PJ - do registro M020 = "00"), que não deverão apresentar esse registro. Somente devem ser referenciadas (registros I051) contas analíticas com natureza de conta (campo COD\_NAT do registro I050) igual a: 01 (contas de ativo); 02 (contas de passivo); 03 (patrimônio líquido) e 04 (contas de resultado), portanto, não devem ser referenciadas (registro I051) as contas de compensação (COD\_NAT = 05) e contas transitórias, que devem ser classificadas como de natureza 09.
* Filial Matriz: informe a Filial Matriz responsável pela escrituração contábil.
* Situação Especial: de acordo com a situação, deve ser selecionada uma das opções: Abertura, Cisão, Fusão, Extinção, Incorporação, ou Nenhum.
* Tipo de Escrituração: selecione o tipo de escrituração. Deverá ser "Centralizada" quando a Matriz for a responsável pelas informações das Filiais vinculadas à sua inscrição, e "Descentralizada" quando cada filial for a responsável por sua contabilização.
* Histórico de Fechamento: Informe o código do Histórico Padrão utilizado na Apuração de Resultado do período (rotina de Transferência de Grupos Contábeis).
* Período de Apuração do FCONT: Anual ou Trimestral (se trimestral, informar os 4 trimestres).
* Copiar arquivo gerado: Após a execução da rotina, o arquivo digital para ser importado no Programa Validador é gerado no caminho indicado na tela. Opcionalmente, pode-se copiá-lo para outro local.

**8º Passo:**  
No Programa Validador da Entrada de Dados do FCONT (PVA – FCONT) liberado pela Receita Federal, importar o arquivo gerado pelo RM Saldus.

**Observação**   
No Programa Validador é necessário sempre mandar importar/substituir todos os Blocos apresentados e que estiverem disponíveis na tela.  
Após a importação da Escrituração, é necessário informar:

* 2 signatários (um deles, obrigatoriamente deve ser o Contador). Este bloco é o J930 do FCONT e o RM Saldus não gera o mesmo automaticamente.
* A Identificação da Qualificação da Pessoa Jurídica. Deve ser informado a qualificação da pessoa jurídica, o tipo de escrituração e o número do recibo anterior se existente, este é o bloco M020 do FCONT.
* A Identificação do Período de Apuração (Anual ou Trimestral e se trimestral, informar os 4 trimestres. Informar também os dados referentes ao Resultado do Período e situação do Resultado do Período, sendo D para débito e C para crédito).
* Opcionalmente (caso não tenham sido incluídos dentro do próprio RM Saldus), incluir os lançamentos com efeito Fiscal.

**9º. Passo:**  
Mandar Verificar Pendências da Escrituração: Se algum erro ou advertência forem encontrados, eles serão apresentados em relatórios e, clicando-se sobre cada um, será aberta a respectiva tela para manutenção.

**10º. Passo:**  
Enviar a escrituração.
