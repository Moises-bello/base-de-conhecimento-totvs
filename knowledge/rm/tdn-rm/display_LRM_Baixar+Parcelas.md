---
content_hash: 6c398da9dca6993abf41dfc8618b11ba19981e24c551113bb5f1e8a2c7bd416c
fetched_at: '2026-06-29T00:09:35.896412+00:00'
page_id: '425459421'
product: rm
source: tdn-rm
title: Baixar Parcelas
type: documentation
url: https://tdn.totvs.com/display/LRM/Baixar+Parcelas
version: 3
---

**Baixar Parcelas**

A Pré-Baixa também faz parte da solução de Integração TOTVS Folha de Pagamento x Gestor AVB (TOOLS) para Averbação (Empréstimo consignado em folha).  A baixa das parcelas será comandada pelo TOTVS Folha no momento da finalização (liberação da competência) do processamento da folha de pagamento (considerando férias, afastamentos, demissões, etc), ou seja, quando esta não for sofrer mais nenhuma alteração todos os empréstimos do tipo AVBTOTVS cadastrados no ERP devem ser enviados para o Gestor AVB (TOOLS). Para isso o ERP efetuará a chamada do serviço de baixa de parcelas que enviará ao TOOLS todos registros de funcionários que tiveram o desconto em folha de seu empréstimo. Este envio será feito através de um Web Service do Gestor AVB. O processo é dividido em três etapas, descritas abaixo, que ajudam o TOOLS a saber quando se inicia e termina a integração do lote.

**Início Envio Pré-Baixa:** Este serviço é chamado apenas uma vez no começo do processamento, para marcar o início do envio dos empréstimos que foram debitados de um determinado mês para o TOOLS.  
    
 **Pré-Baixa:**Será chamado para cada um dos empréstimos do tipo AVBTOTVS localizados na base de dados. Irá informar ao TOOLS as parcelas, o valor que foi efetivamente debitado na folha de pagamento e quando não foi possível debitá-la qual foi o respectivo motivo.  
    
 **Fim Envio Pré-Baixa:**Chamado uma única vez no fim do processamento, para marcar que todos os empréstimos de um determinado CNPJ (coligada) foram enviados. Para cada registro enviado onde o retorno for diferente de SUCESSO, o TOTVS Business Conector deverá gerar um log deste erro e continuar enviando as informações até que o processo seja finalizado.   
    
 ***Nota:*** *Todas as mensagens dos processos de envio e recebimento de informações ficarão gravadas no Monitor da Fila de Integração.*
