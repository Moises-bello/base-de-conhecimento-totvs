---
content_hash: 945b4ee91cd4a52ae5dbd5e707b3393706de6e3080c0a2a0ebf4667de92f675d
fetched_at: '2026-06-29T00:08:07.774556+00:00'
page_id: '237389224'
product: rm
source: tdn-rm
title: Diretório Pré Determinado RM Reports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237389224
version: 17
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é mostrar como é feita a geração de relatórios em diretório predeterminado.

# Introdução:

---

       Foi criado uma funcionalidade para gerar relatórios em um diretório predeterminado, essa funcionalidade foi adicionada através da criação de um parâmetro, no qual deve-se informar o diretório padrão onde o relatório será salvo.

       Também foi adicionado um parâmetro antes da execução do relatório, para permitir que o usuário possa escolher entre "salvar o relatório em um diretório local", ou  "Salvar em um diretório padrão (informado no cadastro)".

# Regra de Negócio:

---

       Foi adicionado dois parâmetros no cadastro do relatório gerado pelo RM Reports, e um parâmetro antes da execução do relatório.

       Se o parâmetro “Salvar no diretório padrão” estiver marcado, é necessário informar o diretório onde o relatório será salvo após sua execução, tal diretório poderá ser local, ou de rede. Em ambos os casos, o departamento de TI do cliente deverá garantir que: o usuário do RM.Host tenha permissão para Ler, Gravar e Modificar arquivos, e que os usuários operadores do sistema não tenham acesso ao diretório escolhido.

       Na execução do relatório, o usuário tem a opção de ignorar o diretório padrão e salvar o relatório em um diretório local de sua escolha.

Observação:

Caso opte pelo diretório local, o relatório será gerado somente no diretório informado. O relatório não será salvo no diretório predefinido, mesmo que esteja parametrizado para isso. Caso o usuário deseje que o relatório seja salvo no diretório definido no cadastro, deverá executá-lo novamente sem marcar essa opção.

       Foram adicionados os seguintes campos na tabela RRptReport:

* USADIRETORIOPADRAO
* DIRETORIOPADRAO.

      No formulário de cadastro de relatórios foram incluídos os controles vinculados aos dois campos citados anteriormente, e um controle para que o usuário possa ignorar o diretório predefinido no formulário de execução do relatório.

Imagens demostrativas abaixo:

Observação:

Caso a opção “Salvar no diretório padrão” esteja desmarcada, o comportamento atual dos módulos não será alterado.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.01.XX

false

**Processo:** RM Reports

falsefalse

**Status:** Finalizado

false

**Data:** 24/05/2016

false

**Autores:**
