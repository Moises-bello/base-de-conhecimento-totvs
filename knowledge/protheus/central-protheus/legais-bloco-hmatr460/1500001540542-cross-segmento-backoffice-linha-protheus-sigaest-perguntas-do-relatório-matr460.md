---
article_id: 1500001540542
category: LEGAIS - BLOCO H/MATR460
content_hash: 3296529f1540a787dae0f9a81332e065d20076b6d46ae79bf132cdfabd66e218
fetched_at: '2026-06-28T22:42:15.194478+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Perguntas do relatório
  MATR460 (Inventário Modelo 7)
type: support-article
updated_at: '2022-01-19T14:41:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001540542-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Perguntas-do-relat%C3%B3rio-MATR460-Invent%C3%A1rio-Modelo-7
---

**Dúvida**

Quais os significados das perguntas do relatório MATR460 (P7)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

O Inventário Modelo 7 (MATR460) é um relatório muito utilizado para pré-visualização dos dados que irão para o Bloco H do SPED, desta forma é muito importante entendermos as condições e critérios que devem ser abordados para ter uma impressão de informações satisfatória.

**OBS:**O relatório MATR460 **não é** um espelho do Bloco K, **mas sim** do Bloco H.

Com isso, verifiquemos abaixo as perguntas e seus significados:

**➢Saldo em Processo?:** Se estiver parametrizado como "Sim", Ordens de Produção (SC2) que possuam movimentações de requisição (Empenho) serão impressas. Ordens de Produções que estiverem abertas, porém sem nenhuma movimentação (RE0/RE1) não serão consideradas

OBS: Se parametrizar esta pergunta como "Sim", deve-se parametrizar a pergunta **Saldo em Fabricação?**= "**Não**", pois quando ambas são parametrizadas como "Sim" o Protheus prioriza o "Saldo em Processo" ou pode gerar duplicidade de dados na impressão.

**➢ Saldo em poder 3°?:**Esta pergunta possui 4 opções de respostas, sendo:

* **Sim:** Imprime Estoque Próprio, Saldo de estoque DE terceiros em nosso poder e Saldo nosso EM estoque de terceiros;
* **Não:**Imprime apenas Estoque Próprio;
* **Em terceiros:**Imprime Estoque Próprio e Saldo de estoque EM terceiros;
* **De terceiros:** Imprime Estoque Próprio e Saldo de estoque DE terceiros em nosso poder.

**➢Armazém Inicial/Armazém Final:**Filtragem dos armazéns a serem considerados na impressão, sendo que, caso utilize MV\_CUSFIL = F, basta parametrizar de "              " à "ZZZZZZZZZ";

**➢Produto Inicial/Produto Final:**Range de produtos a serem considerados na impressão. Caso queira chamar todos os produtos, basta parametrizar de "              " à "ZZZZZZZZZ";

**➢ Produtos Sem Movim. ?**: Caso queria que imprima produto que não teve movimentação no período, selecione como "Sim", caso contrário, como "Não".

OBS: Essa pergunta é pode ter correlação com a pergunta "Lista Produtos C/ Saldo Zerado?", pois em caso de produto sem movimentos, mas com saldo zerado, a depender de como for selecionada a resposta não irá imprimir mesmo que tenha saldo zerado.

**➢ Prods com Saldo** **Neg.?**: Caso o conteúdo seja "Sim", irá imprimir produtos cujo saldo seja negativo. Caso não queira que imprima, selecione como "Não" (esta pergunta só se refere ao saldo físico e não o saldo de custo).

**➢Prods com Saldo Zerado?:**Esta pergunta pode mudar a perspectiva de acordo com a sua parametrização. Basicamente ele imprime ou não produto com saldo zerado. Mas, se tiver um produto com saldo zerado porém com custo "imbutido" neste saldo zerado, não irá imprimir nem saldo nem custo.

**➢Pagina inicial?:**Considera a página inicial do relatório. Fica à critério do usuário.

**➢ Número do Livro?:** Por padrão, é preenchido um \* (asterísco), ou com o número do Livro que o usuário desejar.

**➢ Imprime?:**Selecione "Livro", para que seja impresso o relatório no modelo padrão (Mod 7).

**➢Data de Fechamento:**Esta pergunta quiçá seja a mais importante do relatório. Como este relatório é um espelho do Bloco H, e este é normalmente feito com base no Inventário de 31/12 do ano anterior, parametrize preferencialmente com a data do **último fechamento do estoque.** Para empresas que preferem emitir o relatório para ver de forma sintética os saldos físicos e de custos de seus produtos ao fechar um período, o mais apropriado é delegar a data da virada de saldos neste campo. Desta forma o usuário consegue estabelecer a "régua' de comparação com outros relatórios e tabelas para análise dos saldos físico e financeiro.

**➢ Quanto à descrição?:**Se "Normal", imprime só a descrição, se "Inclui Código", imprimirá Descrição e Código.

**➢ Lista Custo Zerado?**: Esta pergunta tem o mesmo "poder" da pergunta "Lista Saldo Zerado". Ou seja, se estiver = Não e possuir, por algum motivo, produto com saldo porém custo zerado, este saldo não será impresso. Por boa prática, recomendamos marcar esta pergunta como "Sim".

**➢ Lista Custo?:**"Médio" para listar o Custo Médio ou "FIFO" para empresas que utilizam o Custo FIFO.

**➢ Verif. Sld Processo?:** Pergunta para definir se o Saldo em Processo será impresso mediante a Data da Emissão ou Sequência do Cálculo do Custo Médio. Por padrão, o relatório seleciona a opção "Data de Emissão".

**➢ Quanto a quebra por alíquota?:**Esta pergunta permite o usuário selecionar quebra por alíquota, sendo:

* Não quebrar: Não há quebra por alíquota;
* ICMS Produto: Ocorre a quebra por ICMS do Produto;
* ICMS Redução: Ocorre quebra por Redução na Base de Cálculo do ICMS.

**➢ Lista MOD em Processo?**: Esta pergunta é utilizada em conjunto com "Saldo em Processo". Caso queira que imprima requisições para MOD com Saldo em Processo, selecione "Sim". Caso contrário, mantenha como "Não".

**➢ Selecionar Filiais?:** Se "Sim", poderá selecionar as filiais cujos produtos serão impressos com seus respectivos saldos/custos. Se "Não", o Protheus considera a filial que acessou para a impressão.

**➢ Quebrar por Sit. Tributária?:** Esta pergunta permite quebrar ou não o relatório por Situação Tributária, sendo:

* Não: Não realiza a quebra (padrão);
* Sim: Quebra o relatório por situação tributária **desconsiderando** a pergunta "**Quanto à quebra por alíquota**";

**➢ Gerar Arq. Exportação?:** Caso queria gerar o arquivo de exportação para o SPED FISCAL, selecione "Sim". Caso contrário, mantenha como "Não".

OBS: Normalmente é selecionado como "Sim" quando gerado o Bloco H.

**➢ Arquivo Exp. Sped Fiscal?**: Este campo é reservado para delegação da data (em formato americano). Esta data será gerada no arquivo H\_Data+ Grupo + Filial (Ex: H\_2020123199\_01) que será a base para o Bloco H.

OBS: Esta pergunta é validada apenas quando a pergunta anterior (Gerar Arq. Exportação) estiver com conteúdo = Sim.

**➢ Aglutina por CNPJ + IE?:**Caso sim, imprimirá CNPJ + Inscrição Estadual. Por padrão, o relatório traz como "Não".

**➢ Saldo em Fabricação?:**Tem a mesma validação da pergunta "**Saldo em Processo**". Então, se esta pergunta for filtrada como "Sim", a primeira deve ser selecionada como "Não" e vice-versa.

Observações: O MATR460 possui muitos parâmetros que podem mudar a perspectiva de sua impressão. Desta forma, para entender melhor cada um deles e qual a funcionalidade e impacto na impressão do relatório, **[clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901).**

**Saiba mais:**

*[MP - SIGAEST - Dicas de Análise dos Saldos no Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673)*

*[MP - SIGAEST - Parâmetros (SX6) relacionados ao relatório MATR460 - Registro de Inventário Modelo 7](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001351901-MP-SIGAEST-Par%C3%A2metros-SX6-relacionados-ao-relat%C3%B3rio-MATR460-Registro-de-Invent%C3%A1rio-Modelo-7)*

*[MP - SIGAEST - Validação do Parâmetro MV\_R460TPC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001352161-MP-SIGAEST-Valida%C3%A7%C3%A3o-do-Par%C3%A2metro-MV-R460TPC)*

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033001-SIGAEST-LEGAIS)*
