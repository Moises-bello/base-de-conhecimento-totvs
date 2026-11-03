---
content_hash: 1607840faa2e2c43e3a9bc5140440f4c4a8d314dd931f0a33523221f7f31e9d4
fetched_at: '2026-06-29T00:10:07.852806+00:00'
page_id: '452719453'
product: rm
source: tdn-rm
title: Dicas para correção de erros no MANAD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719453
version: 2
---

Seguem os erros e avisos mais encontrados, seguidos de suas soluções:

**Erro**

K050 - Nenhum segurado contribuinte individual foi informado nos registros de cadastro de trabalhadores

**Solução**

Não existe autônomo ou diretor no arquivo. Se realmente não existem casos na empresa ou esses funcionários foram excluídos na geração do arquivo, o erro pode ser desconsiderado.

**Erro**

K050 – PIS/NIT Ausente ou CPF Ausente

**Solução**

Verificar no cadastro do funcionário se está informado o PIS/NIT ou o CPF. No caso de estagiários o cliente pode justificar para o fiscal ou excluí-los da geração do arquivo.

**Erro**

K050, K100, K250 ou K300 campo obrigatório está vazio no arquivo de origem CNPJ\_CEI Solução Se o bloco for o K100, verificar na linha do erro o número da seção informada, editar a seção e verificar se está com o flag "Identificação por CNPJ" marcado. Se for em outro bloco, verificar pela linha do erro a chapa do funcionário. Provavelmente o funcionário está sem histórico de seção.

**Erro**

K200 – Conta não localizada no registro I050 – XXXX (Número da conta) Solução Se também ocorreu o erro de Indicador de Natureza no bloco I050, será resolvido quando informar o indicador de natureza.

**Erro**

K250 ou K300 – Duplicidade de registro (mesma chave de outro registro existente).

**Solução**

Verificar pela linha do erro, a chapa do funcionário e o mês a que se refere. Conferir se existem dados na ficha financeira normal e também na complementar, se estiver nos dois lugares, apagar em um deles.

**Erro**

K250 ou K300 – Trabalhador não localizado no registro K050 - XXXX (Irá aparecer a chapa do funcionário no erro)

**Solução**

Verificar no cadastro do funcionário, aba Registro | Admissão se o tipo de admissão é E ou T (Entrada por transferência). A data da transferência deve existir no histórico de seção para uma seção do mesmo CNPJ que ele está atualmente. Se o tipo de admissão não for E ou T e o campo de data de transferência estiver preenchido, altere o tipo, apague o campo e volte o tipo anterior. Verificar se existe alguma data no campo Data final do contrato, nesta mesma tela.

**Erro**

K250 – Lotação não localizada no registro K100

**Solução**

Resolvendo o erro do Bloco K100 - Campo obrigatório está vazio no arquivo de origem CNPJ\_CEI, esse erro não ocorrerá.

**Erro**

K250 – Data anterior ao período das informações identificado no registro 0000

**Solução**

Ir à linha do erro, localizar a chapa do funcionário. Verificar se é a movimentação de férias. Provavelmente o arquivo está sendo gerado com início, por exemplo, 01/02/2007 e as férias foram pagas com data 29/01/2007. Este é um aviso e pode ser desconsiderado.

**Erro**

K250 - Nenhuma rubrica correspondente localizada no registro K300

**Solução**

Verificar na linha do erro a que se refere o evento no envelope do funcionário. No registro K300 e K250, o 3º campo se refere ao tipo de folha. Se estiver informado 2 é folha de 13°, o restante vai como 1. Se um evento estiver com alguma incidência de 13° salário, verificar se ele possui o código de cálculo correto.

**Erro**

K300 - Rubrica não localizada no registro K150 **Solução** Se tiver ocorrido o erro no K150 de CNPJ não informado, ao corrigir, solucionará este erro.

**Erro**

K300 – Lotação não localizada no registro K100 **Solução** A seção só é levada para o K100 se algum funcionário tiver alocado nela no K050. Se ocorreu o erro de funcionário não localizado no K050, e esse funcionário está nesta seção, ao corrigir o funcionário esse erro é acertado.

**Erro**

I050 – Campo obrigatório está vazio no arquivo de origem – IND Natureza

**Solução**

Preencher a Natureza da conta para a emissão do SPED em Cadastro | Contabilização | Plano de contas contábeis (RM Saldus), editando cada conta.

**Erro**

I050 – Conta superior não localizada no registro I050

**Solução**

O bloco I050 leva o número da conta contábil, no campo ao lado leva a conta superior que é informada pela Procedure. Assim, se a conta é a 01.02.1, a superior é a 01.02. Ela deve existir no Plano de Contas.

**Erro**

K300 - Valor de base de cálculo ds contrib. prev. correspondente não localizada no registro K250

**Solução** O bloco K300 leva os eventos da ficha financeira do funcionário. Verificar na linha do erro, qual evento se refere. Normalmente ocorre em eventos de 13° salário, pois o cliente utiliza eventos com incidências em bases de 13° para pagamento, porém sem código de cálculo com essa finalidade.

**Outras observações:**   
    
 A base levada para o K250 de INSS e IRRF é a soma dos eventos que incidem na competência, ou seja, a base de IRRF não irá conferir com a folha analítica se trabalhar com caixa.  
 Para compor a base é considerada a incidência atual do evento, se ela foi alterada, também não irá conferir com a folha da época.
