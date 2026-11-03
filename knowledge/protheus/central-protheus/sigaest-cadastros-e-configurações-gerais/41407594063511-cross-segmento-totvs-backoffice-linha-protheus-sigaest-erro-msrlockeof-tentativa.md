---
article_id: 41407594063511
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 27c1d73f2b2df3bd666d8bf32a463801666b950d20c76cce086949617e2c3450
fetched_at: '2026-06-28T22:39:09.785309+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Erro MSRLOCK.eof
  Tentativa de reservar o registro Alias em EOF
type: support-article
updated_at: '2026-06-22T18:48:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41407594063511-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-Erro-MSRLOCK-eof-Tentativa-de-reservar-o-registro-Alias-em-EOF
---

A mensagem de erro "MSRLOCK.eof" no TOTVS Protheus indica que o sistema tentou acessar um registro que não existe (EOF - fim de arquivo), geralmente por dados inconsistentes, como códigos inválidos ou exclusões indevidas. Para resolver, deve-se limpar o arquivo de log msrlock.eof, reproduzir o erro, analisar o log gerado para identificar o alias e rotina envolvidos, revisar os dados e desabilitar customizações que possam causar o problema.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41407594044695) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Durante processamentos ou movimentações no sistema, é apresentada a mensagem de erro "MSRLOCK.eof - Tentativa de reservar registro no Alias em EOF" ou "Stack de chamadas em MSRLOCK.eof". O que significa essa mensagem e como tratá-la?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41407594053527)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
A mensagem "EOF Stack em MSRLOCK" ou erro gerado no arquivo "msrlock.eof" não significa que o registro esteja em uso ou bloqueado de forma simultânea por outro usuário. EOF é a sigla para End Of File (Fim de Arquivo).  
  
**Solução**

Essa ocorrência indica que uma rotina (padrão ou customizada) tentou reservar (lock) um registro para processamento, porém o ponteiro da tabela encontrava-se posicionado no final do arquivo (EOF). Ou seja, o sistema tentou processar um registro ou relacionamento que não foi localizado na base de dados.

Na maioria dos casos, isso ocorre devido a dados inconsistentes ou quebra de integridade.

**Exemplos comuns no módulo de Estoque/Custos:**

* Digitação de um código de Produto, Armazém (Local), TES ou Fornecedor/Cliente na movimentação que não está previamente cadastrado ou é inválido.
* Exclusão física de um registro que ainda possui amarrações em tabelas dependentes.
* Customizações (Pontos de Entrada, Gatilhos, Fórmulas) que realizam posicionamento em banco de dados sem a devida validação de sucesso na busca, perdendo o ponteiro do registro principal.

**Para identificar e corrigir a origem do incidente, siga os procedimentos abaixo:**

1. Acesse o diretório "system" do ambiente Protheus (preferencialmente utilizando uma base de Homologação onde o problema ocorra).
2. Localize e exclua o arquivo de log chamado "**msrlock.eof**" para limpar ocorrências antigas.
3. Simule novamente o procedimento no sistema até que o erro seja exibido em tela.
4. Acesse novamente o diretório "**system**" e abra o novo arquivo "**msrlock.eof**" recém-gerado.
5. Verifique dentro do log qual é o Alias (tabela) apontado na falha e analise a pilha de chamadas (stack) para identificar em qual rotina o erro ocorreu, **exemplo abaixo do arquivo, o problema ocorre durante o processo de inclusão do documento de entrada, onde aponta o arquivo SB2 (Tabela de saldos atuais), sendo necessario a avaliação processo em si da criação do documento de entrada.**

   ```
   Data : 22/06/2026 , Hora: 12:00:00
   Arquivo: SB2

   Called from MAAVALPC(4526)
   Called from MAAVALSD1(8689)
   Called from A103GRAVA(15773)
   Called from A103NFISCAL(3852)
   Called from EXECUTE(1149)
   Called from {|| OSELF:EXECUTE("A103NFISCAL"...) }(581)
   Called from ACTIVATE(0)
   Called from ACTIVATE(722)
   Called from FWMBROWSE(10564)
   Called from MBROWSE(173)
   Called from MATA103(312)
   Called from __EXECUTE(735)
   Called from MDIEXECUTE(921)
   ```
6. Revise os dados informados na operação atual. Por exemplo, se o erro ocorreu apontando o Alias SB1 ou SB2, verifique detalhadamente se o produto e o saldo no armazém informados na movimentação estão íntegros e corretamente cadastrados.
7. Se identificar no log que há uma customização (Ponto de Entrada) envolvida no Alias ou na rotina apresentada na mensagem, isole a causa desabilitando a customização temporariamente e valide novamente.

Essas situações são prevista para avaliado do problema, é importante repassar ao suporte padrao, quais ou qual processo, esta sendo efetivamente executado, afim de poder ser possivel a reprodução interna, para analise pontual.

**Detalhes pontuais para analise do seu time de infraestrutura / T.I :**

[Stack de chamadas em MSRLOCK.eof Controle de transaçoes Habilitado](https://tdn.totvs.com/x/vZgKDg)

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
