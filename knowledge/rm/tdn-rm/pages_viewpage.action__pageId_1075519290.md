---
content_hash: 9ff75645c361202c63e5f2125467539e282dc8aa8926119d80c84ef47ef841c6
fetched_at: '2026-06-29T00:05:54.132274+00:00'
page_id: '1075519290'
product: rm
source: tdn-rm
title: Retificação do evento S-1200 quando não há recálculo ou alteração do envelope
  de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1075519290
version: 3
---

### Objetivo

Este documento tem como objetivo orientar o usuário sobre o procedimento de retificação dos eventos do eSocial em situações nas quais a alteração realizada não gera um período de retificação na Folha de Pagamento, ou seja, não ocorre a criação de períodos iguais ou superiores a 10.000.

Esse cenário pode ocorrer, por exemplo, em ajustes de parametrizações do eSocial que não alteram os valores do envelope de pagamento do funcionário, mas exigem a atualização das informações já enviadas ao governo, como alterações de incidência em uma verba.

RetificacaoPasso 1

### Reabertura dos Eventos Periódicos

Antes de iniciar o processo de retificação, é necessário reabrir a competência no eSocial.

#### Procedimento

1. Acesse o menu eSocial | Gerar XML Eventos Periódicos.
2. Selecione a competência que deseja reabrir e marque apenas o evento **S-1298 - Reabertura dos Eventos Periódicos**.
3. Avance pelas etapas do processo até concluir a geração do XML.
4. Após a geração, acesse a **Fila de Eventos** e realize a integração/transmissão do evento **S-1298**.
5. Aguarde o retorno do governo e confirme que o evento **S-1298** foi processado com sucesso.
6. Somente após a aceitação do **S-1298** prossiga com os demais procedimentos de retificação dos eventos periódicos.

### .

Passo 2

### Verificar a necessidade de exclusão do evento S-1210

Conforme regra do eSocial, a retificação de um evento S-1200 somente será aceita quando houver compatibilidade entre o valor líquido informado no S-1200 e o valor declarado no respectivo S-1210.

Por isso, antes de iniciar a retificação, é importante avaliar se a alteração realizada impacta o valor líquido já enviado ao governo. Caso não haja alteração no valor líquido, não será necessário excluir o S-1210.

Entretanto, se a alteração provocar divergência entre os valores informados nos eventos S-1200 e S-1210, será necessário excluir previamente o S-1210 por meio do evento S-3000 (Exclusão) antes de realizar a retificação do S-1200.

#### Procedimento

1. Acesse eSocial | Eventos da Folha.
2. Localize e selecione o(s) evento(s) **S-1210** relacionado(s) ao **S-1200** que será retificado.
3. Selecione Processos | Gerar Evento de Exclusão (S-3000).
4. Gere e transmita o evento **S-3000** ao eSocial.
5. Aguarde o processamento com sucesso do evento antes de prosseguir com a retificação do **S-1200**.

Passo 3

### Ajustes de incidência na verba

Após realizar os ajustes necessários na verba, como alterações de incidências, o sistema gerará automaticamente um gatilho do evento **S-1010** na fila de eventos.

Caso essa alteração seja retroativa a competência anterior à atual, ajuste a competência (início de validade) do evento gerado.

Para isso, poderá ser utilizada a rotina **"Atualizar competência da fila de eventos S-1010"**, que permite alterar em lote o início de validade dos eventos, informando a competência desejada.

Após a conferência da competência, será necessário enviar a atualização ao governo por meio do evento **S-1010 - Tabela de Rubricas**.

#### Procedimento

1. Verifique o evento **S-1010** gerado na fila de eventos.
2. Caso necessário, ajuste a competência utilizando o processo **"Atualizar competência da fila de eventos S-1010"**.
3. Gere e transmita o evento **S-1010** referente à verba alterada.
4. Aguarde o retorno do governo e confirme que o evento foi processado com sucesso.
5. Somente após a aceitação do **S-1010**, prossiga com a retificação dos eventos periódicos.

**Importante:** Este ajuste pode ser realizado antes ou depois da reabertura dos eventos periódicos (S-1298), pois a ordem de execução dessas etapas não impacta o resultado do processo.

Passo 4

### Geração e envio da retificação do S-1200

Após a atualização da rubrica e a aceitação do evento **S-1010** pelo governo, realize a geração da retificação do **S-1200**.

#### Procedimento

1. Acesse eSocial | Eventos da Folha.
2. Localize e selecione os eventos **S-1200** que deverão ser retificados.
3. Selecione Processos | Gerar Retificação Arquivo eSocial.
4. Gere os eventos de retificação.
5. Acesse a fila de eventos e realize a integração/transmissão dos eventos **S-1200** ao governo.
6. Aguarde o retorno e confirme o processamento com sucesso antes de prosseguir para as próximas etapas.

Passo 5

### Geração e envio da retificação do S-1210

Após a aceitação da retificação do **S-1200**, realize a geração do evento **S-1210 - Pagamentos de Rendimentos do Trabalho**.

#### Procedimento

1. Acesse eSocial | Gerar XML (Eventos Periódicos).
2. Selecione a competência desejada.
3. Marque apenas o evento **S-1210 - Pagamentos de Rendimentos do Trabalho**.
4. Execute o processo de geração do XML.
5. Após a geração, acesse a fila de eventos e realize a integração/transmissão do **S-1210** ao governo.
6. Aguarde o retorno e confirme o processamento com sucesso do evento.

Passo 6

### Fechamento dos Eventos Periódicos

O sistema não realiza a geração automática de um novo evento **S-1299 - Fechamento dos Eventos Periódicos** após o processo de retificação.

Dessa forma, para efetuar novamente o fechamento da competência, será necessário incluir manualmente o evento **S-1299** na fila de eventos, gerar o XML correspondente e realizar sua transmissão ao governo.

Após o envio, aguarde o retorno do eSocial e confirme o processamento com sucesso do evento **S-1299**, garantindo assim o fechamento da competência.

Passo 7

### Conferência das bases de cálculo

Após a conclusão dos envios e retornos dos eventos do eSocial, gere os relatórios de conferência e valide as bases de cálculo apresentadas nos retornos do governo, comparando-as com as bases apuradas na Folha de Pagamento.

Essa validação é importante para garantir que as informações enviadas e processadas pelo eSocial estejam consistentes com os valores calculados pelo sistema, permitindo identificar e corrigir eventuais divergências antes do fechamento da competência.

#### Relatórios recomendados para conferência

Utilize os relatórios abaixo para validar as bases de cálculo e os valores retornados pelo eSocial:

* [Relatório de Conferência IRRF S-5002](https://tdn.totvs.com/pages/viewpage.action?pageId=1028947938)
* [Relatório de Conferência de FGTS](https://tdn.totvs.com/pages/viewpage.action?pageId=536720973)
* [Relatório de Conferência de INSS](https://tdn.totvs.com/pages/viewpage.action?pageId=536721262)
* [Relatório de Conferência INSS Patronal](https://tdn.totvs.com/pages/viewpage.action?pageId=714242305)

---
