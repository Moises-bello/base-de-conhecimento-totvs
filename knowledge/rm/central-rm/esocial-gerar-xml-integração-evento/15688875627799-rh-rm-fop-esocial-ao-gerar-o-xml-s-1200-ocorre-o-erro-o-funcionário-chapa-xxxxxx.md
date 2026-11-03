---
article_id: 15688875627799
category: eSocial - Gerar XML/ Integração Evento
content_hash: 6e080fce559486bdb836376faba36b463777f4ba69871988022d4a37abcba78a
fetched_at: '2026-06-28T22:47:11.930720+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao gerar o XML S-1200 ocorre o erro: O funcionário
  chapa ''XXXXXX'' está afastado e o evento com CC315 não foi lançado'
type: support-article
updated_at: '2026-01-02T17:17:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15688875627799-RH-RM-FOP-eSocial-Ao-gerar-o-XML-S-1200-ocorre-o-erro-O-funcion%C3%A1rio-chapa-XXXXXX-est%C3%A1-afastado-e-o-evento-com-CC315-n%C3%A3o-foi-lan%C3%A7ado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15688904502551) Tempo aproximado para leitura: **01:30:00 min**  
  
**Ocorrência**  
Ao gerar o XML S-1200 ocorre o erro: O funcionário chapa '004787' está afastado e o evento com CC315 não foi lançado.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Esse incidente ocorre ao gerar o XML S-1200 de um funcionário que está afastado e no envelope não consta o evento com código de calculo 315.   
  
**Solução**

Considera-se base de cálculo apenas para **apuração do FGTS**, o pagamento ao trabalhador afastado por **acidente de trabalho** (a partir do 16º dia), **serviço militar obrigatório** e**salário maternidade**. Na hipótese em que o salário maternidade é pago à empregada do **MEI**, diretamente pela Previdência Social, deve ser informado, em rubrica de natureza informativa correspondente, o valor relativo à remuneração a que teria direito, se em atividade, durante o período de afastamento.

O **Anexo II - Tabela de Regras** do leiaute do eSocial informa que todos os trabalhadores admitidos em período igual ou anterior ao período de apuração que não estejam desligados, cujo desligamento ou baixa judicial seja posterior ao período de apuração, devem possuir o respectivo evento de remuneração já encaminhado para o mesmo período de apuração, **com algumas exceções a serem observadas na imagem abaixo**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15688899152791)

Para o funcionário afastado, deve conter no envelope de pagamento a verba de **código de cálculo 315 - Base de FGTS de Afastados** para o envio no S-1200. O lançamento da verba para o envelope de pagamento é **automático**e realizado no momento do lançamento dos códigos de cálculos **1 - Horas Normais, 2 - Dias Trabalhados** ou **145 - Atestado Médico**, quando identificado que o funcionário possui o **afastamento registrado**(Acidente de Trabalho, Serviço Militar ou Doença Ocupacional)**no mês corrente**. Depois, na [Geração dos Eventos Periódicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003044711-RM-eSocial-Gera%C3%A7%C3%A3o-dos-eventos-peri%C3%B3dicos?source=search) selecione a situação dos funcionários que possuem a verba lançada no envelope de pagamento.   
Para empresas que utilizam **Tomadores de Serviço**, é necessário realizar a **Distribuição de SEFIP**antes da geração do XML periódico.

**Saiba mais**  
Para mais informações acesse:

      •  [Código de Cálculo 315 – BASE DE FGTS DE AFASTADOS](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719616)  
      •  [Relação do tipo de afastamento x motivo de afastamento eSocial](http://tdn.totvs.com/display/LRM/Evento+S-2230)   
      •  [RH - RM - FOP - eSocial - Envio do evento S-1200 mensal para funcionários afastados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037949633-RH-RM-FOP-eSocial-Envio-do-evento-S-1200-mensal-para-funcion%C3%A1rios-afastados?source=search)
