---
content_hash: 60a24a1a690701ac5d92ca1dea452afc94ce435692be13b3ddac2301c32cef80
fetched_at: '2026-06-29T00:11:29.222980+00:00'
page_id: '734381204'
product: rm
source: tdn-rm
title: Relatório - Conferência de INSS Patronal - Como validar divergências?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=734381204
version: 10
---

# Objetivo:

---

       O objetivo deste documento é orientar como validar divergências entre os valores gerados pelo TOTVS Folha de Pagamento e retornados pelo Governo no Relatório de Conferência do INSS Patronal.

Informações

A partir dos Patches:

* 12.1.2209.151 ou Superiores.
Agrupador DadosApresentação e Configuração do Relatório

O Relatório de Conferência de INSS Patronal está disponível tanto para clientes que utilizam o Middleware quanto para aqueles que usam o TAF Padrão.

Entretanto, para correta utilização dos relatórios de conferência é necessário algumas premissas:

* RM e TAF atualizados
* Configuração de servidor e porta APP e API no parametrizador do eSocial
* Liberação de acesso ao menu do relatório nos perfis do usuário
* Configuração do histórico de INSS no cadastro de seção

Na documentação abaixo constam todas as orientações e detalhamentos para uso do relatório:

* [Relatório de Conferência INSS Patronal](https://tdn.totvs.com/pages/viewpage.action?pageId=714242305)
Validação de Divergências

Antes de executar e utilizar o Relatório de Conferência de INSS Patronal, sugerimos que seja validado o Relatório de Conferência de INSS/FGTS, avaliando os resultados individuais dos funcionários.

Abaixo segue a documentação do Relatório de Conferência de INSS/FGTS para auxílio:

* **MIDDLEWARE**
  + [Middleware - Relatório de Conferência de INSS](https://tdn.totvs.com/pages/viewpage.action?pageId=536721262)
  + [Middleware - Como validar divergências no relatório comparativo](https://tdn.totvs.com/pages/viewpage.action?pageId=566476942)

* **TAF PADRÃO**
  + [Painel de Conferência de INSS](https://tdn.totvs.com/pages/viewpage.action?pageId=528452133)

**Somente após não constatar nenhuma divergência no relatório de INSS por funcionário, gerar o relatório patronal e realizar suas validações.**

Validação\_RelExportação do Relatório

Após gerar o Relatório de Conferência de INSS Patronal, o ideal é que seja realizada a exportação do relatório para, então, verificar as possíveis divergências apontadas.

Para realizar a exportação, basta clicar em "**Exportar CSV**":

Após, clique em "**Abrir arquivo**":

Será gerado um arquivo com a extensão ".CSV" trazendo uma divisão de abas, da seguinte forma:

* **Total Empresa:**Traz os valores dos Card's totalizadores.
* **Estabelecimentos:** Retorna os valores analíticos da parte de estabelecimentos do relatório.
* **Valores Estabelecimentos:**Retorna os valores por códigos de receitas detalhados por estabelecimento.
* **Lotações:** Retorna os valores analíticos da parte de lotações do relatório.
* **Valores Lotações:** Retorna os valores das bases detalhados por lotação.

1 - Total Empresa

AVALIAR NECESSIDADE DESSA ABA

2 - Estabelecimentos

Na aba "2 - Estabelecimentos" do relatório exportado, serão apresentados os valores analíticos dos estabelecimentos.

Nos estabelecimentos listados, verifique a coluna "**Divergente**". Caso ela esteja com o valor "**FALSO**", significa que **tanto a Folha quanto o RET (governo) estão com informações compatíveis**. Caso o valor apontado na coluna "Divergente" seja "**VERDADEIRO**", verifique campo a campo qual das informações está incorreta e veja abaixo onde no sistema ajustar:

**CNAE Folha**

Abra o menu "Administração de Pessoal | Seções" e faça a edição da seção centralizadora correspondente. Valide na aba "RAIS / CAGED / eSocial" o campo "CNAE Preponderante".

**CNAE RET**

Abra o menu "eSocial | Fila de Eventos" e faça a edição do S-1005¹ vinculado à seção centralizadora correspondente. Verifique o valor gerado na tag "cnaePrep".

Alíquota RAT Folha

Abra o menu "Administração de Pessoal | Seções" e faça a edição da seção centralizadora correspondente. Valide na aba "Dados p/ INSS" o campo "%Acid.Trabalho".

Alíquota RAT RET

¹ Fique atento a possibilidade de existir mais de um S-1005 para a mesma seção, devido a data de início de vigência. Importante que seja validado o S-1005 que esteja vigente dentro do período de apuração selecionado na geração do relatório.
