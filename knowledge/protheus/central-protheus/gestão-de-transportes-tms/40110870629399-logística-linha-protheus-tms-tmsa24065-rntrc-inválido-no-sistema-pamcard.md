---
article_id: 40110870629399
category: Gestão de Transportes (TMS)
content_hash: e1b17d9b0709b5d9586fa8d2f7187bdba43199d9e28d5686bccfe28f5e7f7b3e
fetched_at: '2026-06-28T22:45:27.209973+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS -  TMSA24065 - RNTRC Inválido no Sistema Pamcard
type: support-article
updated_at: '2026-04-30T13:26:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40110870629399-Log%C3%ADstica-Linha-Protheus-TMS-TMSA24065-RNTRC-Inv%C3%A1lido-no-Sistema-Pamcard
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40110881310487) Tempo aproximado para leitura: **00:01:55 min**  
  
**Dúvida**  
O que é o *help* **TMSA24065  - RNTRC Inválido no Sistema Pamcard** e como resolver?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**  
A mensagem **TMSA24065 - RNTRC Invalido no Sistema Pamcard** ocorre quando o Sistema consulta o **RNTRC** do fornecedor na Pamcard e não obtemos um retorno positivo de **RNTRC** válido.  
  
Se essa mensagem ocorre, consulte o **RNTRC** em [Consulta Pública ANTT - Consulta RNTRC](https://consultapublica.antt.gov.br/Site/ConsultaRNTRC.aspx) e valide se ele está ativo e válido para o proprietário do veículo.

* Se o **RNTRC** estiver inválido ou inativo, é preciso ajustar o **RNTRC** no cadastro do fornecedor no campo **A2\_RNTRC**.
* Se o cadastro estiver válido, é possível que tenha ocorrido alguma falha na consulta do **RNTRC** na integração do TMS com a Pamcard, e para isso é preciso avaliar os logs da integração. Para gerar os logs da integração na pasta **/system/** é necessário ativar o parâmetro **MV\_TMSXML**.   
  Em nosso histórico, uma falha comum de ocorrer nessa consulta é quando está implantando a integração em uma filial que não é a contratante e ocorre o erro **Empresa não existe** no retorno da Pamcard no **XML**. Quando utiliza uma filial que não é a contratante para integrar com a Pamcard, é necessário preencher o campo**Filial Contr -** **DEG\_FILCTR**com a filial contratante para que a integração funcione.  
  Caso ocorra outro erro no XML e não consiga identificar a causa, recomendamos que entre em contato com nosso time de suporte e envie os **XMLs** gerados na integração.

Glossário  
**RNTRC** - Registro Nacional de Transportadores Rodoviários de Cargas  
**XML** - *Extensible Markup Language*
