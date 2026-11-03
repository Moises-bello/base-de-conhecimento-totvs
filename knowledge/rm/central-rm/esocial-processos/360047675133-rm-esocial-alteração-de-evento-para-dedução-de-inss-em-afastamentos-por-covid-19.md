---
article_id: 360047675133
category: esocial - Processos
content_hash: 8efe6704496c14842e4174acd99d4a858fd8b11e2c2a2d3af0306ad95eb66736
fetched_at: '2026-06-28T22:47:08.449083+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: RM - eSocial - Alteração de evento para dedução de INSS em afastamentos por
  Covid-19
type: support-article
updated_at: '2021-04-09T12:27:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047675133-RM-eSocial-Altera%C3%A7%C3%A3o-de-evento-para-dedu%C3%A7%C3%A3o-de-INSS-em-afastamentos-por-Covid-19
---

**Ocorrência**  
Foram enviados ao eSocial o **S-1010** com **Natureza de Rubrica 9933** (Auxílio Doença) e **codIncCp 51** conforme orientação da **Nota Orientativa 2020/21**. Posteriormente, enviado a folha de pagamento com a verba cadastrada. Porém, no ambiente do governo não ocorreu a dedução do INSS nos 15 primeiros dias de afastamento.  
  
**Ambiente**  
RM - eSocial - A partir dos *Patches* 12.1.25.271, 12.1.26.217, 12.1.27.173 e 12.1.28.107  
  
**Causa**  
Conforme a **NO 2020.21**, as empresas estão autorizadas a deduzirem de suas contribuições devidas à previdência social os valores pagos em relação aos 15 primeiros dias de salário do trabalhador afastado por enfermidade causada pelo Covid-19.

Para atender **NO 2020.21** foram liberados os códigos de cálculos (CC) **436-ATESTADO MÉDICO DE AFASTAMENTO POR COVID-19** e **437-DIFERENÇA DE ATESTADO MÉDICO POR COVID-19**.

Porém houve a necessidade de realizar uma modificação na geração do evento **S-1010** para que na tag **TpRubr** seja levado **3-Informativa** ao invés de ser levado **4-Informativa Dedutora**, com isso ocorrerá a dedução do valor desta rubrica na DCTFWeb, conforme orientação do governo.  
  
**Solução**  
Caso o usuário tenha enviado o evento **S-1010** das verbas criadas (CC 436 e 437) ou o evento **S-1200** antes das versões citadas acima na área **Ambiente**, será necessário realizar a retificação destes eventos.   
Siga abaixo o passo a passo para retificação:

1. Acesse o menu **eSocial | Fila de Eventos** e clique em **Incluir**;  
1.1. Cadastre um gatilho de alteração do evento **S-1010** para as verbas com o código de cálculo **436** e código de cálculo **437**. Selecione a mesma competência em que foi enviado o seu evento e cadastre o tipo da operação como **Alteração**;  
1.2. Gere os XML's e transmita os eventos para o governo.   
2. Após o aceite do governo nos eventos **S-1010**, acesse o menu **eSocial | Eventos Periódicos**;  
2.1. Selecione o evento **S-1200** do(s) funcionário(s) que deseja retificar, e clique em **Processos | Gerar Retificação Arquivo eSocial**. Será gerado na fila um gatilho de retificação para cada um dos funcionários selecionados.  
2.2. Gere os XML's e transmita os eventos para o governo. 

**Importante**  
Caso já tenha sido enviado o evento S-1210 para os funcionário, deve-se realizar a exclusão deste evento antes de enviar a retificação do S-1200.  
  
**Saiba mais**  
Para mais informações, acesse:  
      • [Como gerar a correção da dedução do Afastamento Empregado COVID-19](https://tdn.totvs.com/pages/releaseview.action?pageId=547236037)  
      • [NO 2020.21 - Afastamento Empregado Covid-19](https://tdn.totvs.com/display/public/LRM/NO+2020.21+-+Afastamento+Empregado+Covid-19)
