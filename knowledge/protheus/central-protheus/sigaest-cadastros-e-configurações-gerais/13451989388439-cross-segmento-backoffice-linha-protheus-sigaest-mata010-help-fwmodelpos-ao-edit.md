---
article_id: 13451989388439
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 87f863d77a9ab2ce63d4a2f240a8630157280578d12fbf99c97d6690ac5fa07d
fetched_at: '2026-06-28T22:39:09.499520+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - HELP FWMODELPOS
  ao editar um produto. Como resolver?
type: support-article
updated_at: '2024-06-10T18:06:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13451989388439-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-HELP-FWMODELPOS-ao-editar-um-produto-Como-resolver
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24002408408855) Tempo aproximado para leitura: **00:04:00 min****Ocorrência**Na rotina ***CADASTRO DE PRODUTOS (MATA010)*** ao editar um produto e salvar, apresenta o **HELP FWMODELPOS** impedindo a conclusão da edição. Como resolver?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13452179529751)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**Esse Help está frequentemente relacionado a alguma inconsistência nos dicionários de dados, que ao ser processado, impossibilita a conclusão da rotina.

Veja a seguir as principais inconsistências mapeadas que tendem a gerar esse problema, e valide cada item pontualmente para localizar a origem do problema em seu ambiente, e sanar o Help.

**Solução**

Recomendamos que baixe em ambiente Teste os dicionários [completo](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/BRA-dicionarios_compl) e [diferencial](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/BRA-dicionarios_dif) para ter como base os dicionários padrões/nativos, nos quais não deve ocorrer erro.

Tendo baixado esses dicionários em ambiente teste, será possível conferir com seu ambiente, no qual ocorre o erro, a fim de localizar as inconsistências locais e corrigir.

**1ª - Campos que tiveram sua ordem indevidamente desposicionada:**

No Protheus, ao acessar o módulo Configurador > Base de Dados > Dicionário > Bases de Dados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24002408442775)

Após isso Selecionar "Dicionário de Dados" e Pesquisar a Tabela SB1 e editar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24002408455703)

É possível visualizar os campos da tabela :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24002395017495)

Podemos visualizar a ordenação dos campos do cadastro de produto e identificar campos com indicador vermelho (campo com ordem travada pelo sistema) e campos com indicador verde (campo com ordem liberada). O configurador não permite a alteração de campos com legenda vermelha e se por algum motivo é realizado esse tipo de processo "forçado" (Via APSDU ou Banco de dados) esse Help será apresentado.

Qualquer campo indevidamnte desposicionado pode causar o problema. Apenas para referência, a principal recorrência que temos sobre esse tipo de alteração no cadastro de produtos é dos campos **FORNECEDOR (B1\_PROC)** e **LOJA FORNECEDOR (B1\_LOJPROC)** os quais devem estar posicionados sequencialmente.

Segue print exemplificando:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13452311779735)

**2° - Consulta Padrão errada ou inexistente:**

Outra causa mapeada é a consulta padrão dos campos. Já foi identificada recorrência de campos com sua Consulta padrão indevidamente configurada ou ausente. Um dos campos recorrentes é o B1\_POSIPI conforme [detalhes aqui](https://tdn.totvs.com/x/wMt-Hw)

Recomendamos que configure a consulta padrão corretamente, de acordo com os dicionários padrões/nativos.

**3° - Gatilho ou Validações de usuário customizados:**

O Protheus disponibiliza a possibilidade de criação de gatilho em diversos campos de diversas tabelas e a SB1 não é diferente, dessa maneira, caso tenha gatilhos ou validações fora do padrão dentro de seu dicionário, é interessante realizar teste com um dicionário padrão, garantindo que nenhum deles esteja impactando no resultado.

**4° - Ponto de Entrada dentro da rotina MATA010**

A rotina MATA010 dá a possibilidade de utilizar Pontos de entrada, e a mensagem **FWMODELPOS** pode estar relacionada com a existência de ponto de entrada em MVC com alguma falha relacionada ao modelo. Para maiores informações sobre os Pontos de Entrada em MVC [clique aqui](https://tdn.totvs.com/x/6rcDIQ). Recomendamos realizar teste com dicionários padrões/nativos (sem chamada de customizações via dicionário) e com RPO padrão, garantindo que nenhuma customização esteja ocasionalmente impactando no resultado.

**5° - Arquivos de Help Desatualizado**

Pode ocorrer de os arquivos de Helps do ambiente estarem desatualizados, e nesse caso, que o Help apresentado não seja a realidade dentro da validação do fonte MATA010, levando a uma análise equivocada. Dessa maneira, uma recomendação é realizar a atualização dos Helps apenas para garantir que estamos mapeando o Help correto ([como atualizar arquivos de helps](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028969891-Framework-Linha-Protheus-FRAME-Atualiza%C3%A7%C3%A3o-de-Help)).

**HELPS DE CAMPOS/PERGUNTAS COMPLETO BRASIL:** [12.2210](https://suporte.totvs.com/portal/p/10098/download?e=1083929%C2%A0) | [12.2310](https://suporte.totvs.com/portal/p/10098/download#detail/1112211)

**HELPS DE CAMPOS/PERGUNTAS DIFERENCIAL BRASIL:**[12.2210](https://suporte.totvs.com/portal/p/10098/download?e=1083852) | [12.2310](https://suporte.totvs.com/portal/p/10098/download#detail/1112212)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**IMPORTANTE:**

Conforme explicado no início, essa ocorrência está frequentemente ligada à inconsistências nos dicionários de dados do ambiente no qual apresenta o Help. Recomendamos que valide o processo com os dicionários padrões/nativos, baixando os arquivos [completo](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/BRA-dicionarios_compl) e [diferencial](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/BRA-dicionarios_dif) em ambiente Teste.

Caso o problema persista, acione o Suporte técnico enviando o parecer destas validações já realizadas, e enviando também o log de [Stack de Funções](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10837549101335-MP-SIGALOJA-Como-gerar-Stack-de-fun%C3%A7%C3%B5es) para análise. Verifique com o Suporte a disponibilidade para Consultoria, a fim de rastrear em seu ambiente as particularidades para ocorrência do help.

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
