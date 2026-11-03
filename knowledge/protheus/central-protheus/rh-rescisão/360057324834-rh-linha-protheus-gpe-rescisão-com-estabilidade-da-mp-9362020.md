---
article_id: 360057324834
category: RH - Rescisão
content_hash: 55cb4ded780abcc3b333f58eb5bc8ce1f9c4237c32d559313cf5399a08eba269
fetched_at: '2026-06-28T22:43:54.422641+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Rescisão com estabilidade da MP 936/2020
type: support-article
updated_at: '2022-08-25T18:54:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057324834-RH-Linha-Protheus-GPE-Rescis%C3%A3o-com-estabilidade-da-MP-936-2020
---

**Ocorrência**A Lei nº 14.020/2020 (antiga MP 936/2020) prevê no artigo 10 uma garantia provisória ao trabalhador durante o período acordado da redução da jornada de trabalho e do salário ou da suspensão temporária do contrato de trabalho ou após o reestabelecimento da jornada de trabalho e do salário ou do encerramento da suspensão temporária do contrato de trabalho por período equivalente ao acordado para a redução ou a suspensão.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução**Foi implementado o cálculo e pagamento da indenização da garantia provisória prevista no artigo 10 da Lei 14.020/2020 (antiga MP 936/2020) no ID de cálculo **1853** ao efetuar o cálculo da rescisão.  
  
Deverá ser executado UPDDISTR para criação do campo abaixo (dicionário diferencial consta na Expedição Contínua do Portal):  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099515833/mceclip0.png)  
  
**Passo1:**Há algumas pré-condições:

1. O mnemônico **P\_LPPEATIV**deve estar **ativado**, isto é, com configuração **.T.**.
2. O campo **RG\_DTESTAB** deve existir no dicionário de dados sistema.
3. A rescisão não pode ser por justa causa ou a pedido do funcionário. O sistema efetua essa identificação através da configuração do tipo de rescisão na tabela S043, através do campo "Cod. Afast. FGTS", que não poderá estar preenchido com  "H" nem "J".
4. Deve haver uma verba cadastrada para o ID de cálculo **1853:**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097211054/mceclip1.png)  
     
   Como **sugestão**, a verba deverá ter incidência para FGTS.

**Passo 2:**O sistema irá verificar a configuração do mnemônico **P\_PRJESTAB**. Se estiver **desativado**, isto é, configurado com **.F.**, o sistema irá projetar os dias do aviso indenizado a partir da data do aviso prévio (conceito atual); se estiver **ativado**, isto é, configurado com **.T.**, o sistema irá projetar os dias do aviso indenizado a partir da data de término da estabilidade, caso a data da estabilidade for superior a data do aviso, senão continuará a projetar os dias do aviso a partir da data do aviso prévio.

Por exemplo, se o funcionário tem 33 dias de aviso prévio indenizado, a data do aviso prévio for 25/09 e o término da estabilidade ocorrer em 30/10, caso o mnemônico esteja **ativado**, o sistema irá projetar o aviso até a data de **02/12**; caso esteja **desativado**, o sistema irá projetar o aviso até a data de **28/10**.

Observe que essa configuração pode alterar os avos de férias sobre aviso e 13º sobre aviso que o funcionário receberá no cálculo da rescisão.

Há o entendimento da consultoria tributária (disponível em [MP 936/2020 - Lei 14.020 - Indenização da Garantia Provisória](https://tdn.totvs.com/pages/viewpage.action?pageId=558261771)) que afirma que a projeção do aviso indenizado deve iniciar a partir do término da estabilidade, então por **padrão** o mnemônico estará **ativado**. Caso não possua o mesmo entendimento e deseje que o sistema continue a utilizar o conceito antigo, basta alterar a configuração do mnemônico, alterando o cadastro do mnemônico e desativando-o.

**Passo 3:**O sistema irá verificar na tabela de histórico de contrato se houve redução de jornada e suspensão do contrato de trabalho na tabela de ausências. A Lei garante uma estabilidade durante a redução ou suspensão e após o término da redução ou suspensão pelo mesmo período que foi acordado.

Por exemplo: se houve um acordo de redução de jornada de 01/09 a 30/09, ou seja, de 30 dias, o término da estabilidade será de 30 dias após o término, ou seja, a estabilidade irá até 30/10.

Há algumas exceções:

1. Se o campo Status (RGE\_STATUS) da tabela de histórico de contrato estiver preenchido com **1** ou **2** (Inativo/Cancelado), a redução de jornada será **ignorada**;
2. Se o campo Status (RGE\_STATUS) da tabela de histórico de contrato estiver preenchido com **4** (Reduzido), o término da estabilidade irá considerar a data de término acordada originalmente e não a data antecipada, conforme entendimento da consultoria tributária disponível em [MP 936/2020 - Contagem da estabilidade /antecipação acordo](https://tdn.totvs.com/pages/viewpage.action?pageId=547868618).

Obs.: caso o funcionário possua redução de jornada e suspensão do contrato no histórico, o sistema irá considerar o que ocorrer por último.

Quando for iniciado o cálculo da rescisão e a data de rescisão for inferior à data do término da estabilidade, o sistema exibirá o alerta abaixo, para que o usuário se atente e confirme se o cálculo da rescisão deve ser realmente efetuado:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097211154/mceclip2.png)  
  
  
**Passo 4:** Se a data de rescisão for inferior à data do término da estabilidade, o sistema irá apurar a indenização da garantia provisória na verba de ID **1853.**

Por exemplo, se a rescisão for efetuada em 25/09 e o funcionário tinha uma redução de jornada de 01/09 a 30/09 de 25%, ou seja, com término da estabilidade em 30/10, o sistema irá calcular uma indenização de 36 dias (25/09 a 30/10) de 50%. Se o funcionário recebe salário mensal de R$ 1.200,00, sua indenização será de R$ 720,00 ( 50% X (R$ 1.200,00 ÷ 30 X 36)).

**Importante:**  
Através da configuração da verba do ID **1853** no campo Base Cálculo (RV\_BASCAL), se o mesmo estiver configurado com **2**, o sistema irá utilizar o salário **incorporado**; caso contrário irá utilizar o salário **base**.

Caso o mnemônico **P\_ADIMULMP** esteja ativo, o sistema também irá considerar o valor dos adicionais de salário (periculosidade, insalubridade, adicional por tempo de serviço, adicional de confiança e/ou adicional de transferência) na base de cálculo da indenização.

Além disso, o sistema também irá verificar a configuração do mnemônico **P\_RESMULTH** para funcionários de categoria Horista, conforme explicado com mais detalhes na documentação disponível em [3751785 DRHPAG-20800 Multa por Contrato de Experiência p/ Horista](https://tdn.totvs.com/pages/viewpage.action?pageId=515690732).

Obs.: esses conceitos são os mesmos adotados nas indenizações por rescisão antes do término de contrato de experiência ou do término do contrato determinado.

Caso haja algum entendimento diverso da forma de apuração do valor da indenização da garantia provisória, é possível utilizar como base a fórmula **S\_INDMP936**. Dessa forma, basta copiá-la e alterá-la conforme necessidade, desabilitar a fórmula padrão no roteiro RES e incluir a fórmula customizada.

**Atenção** se o % na tabela S61- PPE Prog Proteção Emprego e tabela RGE campo % Redução "RGE\_PERC" sistema não irá gerar a verba com id 1853.

**Saiba mais:** [Expedição Continua RH Protheus](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
