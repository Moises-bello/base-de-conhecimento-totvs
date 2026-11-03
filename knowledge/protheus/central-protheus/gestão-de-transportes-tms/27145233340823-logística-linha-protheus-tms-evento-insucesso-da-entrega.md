---
article_id: 27145233340823
category: Gestão de Transportes (TMS)
content_hash: 245f34f6126156c790bd6cdc327ef8f9912de070e516baa5a512bf134361bd2e
fetched_at: '2026-06-28T22:45:27.740785+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Evento Insucesso da Entrega
type: support-article
updated_at: '2026-04-17T16:34:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27145233340823-Log%C3%ADstica-Linha-Protheus-TMS-Evento-Insucesso-da-Entrega
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27145242296983) Tempo aproximado para leitura: **00:04:40 min**  
  
**Dúvida**  
Como registrar evento de Insucesso de Entrega no **SIGATMS - Gestão de Transportes**?   
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**  
Realizado ajuste para geração, manutenção e transmissão do novo **Evento de Insucesso** para a **SEFAZ - Secretaria da Fazenda**.  
Para utilização desta inovação/legislação, caso esteja na release **12.1.2310 ou anterior**, será necessário primeiramente atualizar o ambiente com os pacotes de atualização do **TSS** e **TMS** que estão listados em **Saiba mais e** aplicar o pacote de dicionários **012767** para criação da tabela **DNN - Evento de Insucesso na Entrega** que está em anexo. Na release **12.1.2410**, estas atualizações já estão no padrão.  
  
Com o ambiente devidamente atualizado, é preciso validar as seguintes parametrizações:

Acesse a rotina **TMSA020 - Tabela de Ocorrências**, através do fluxo: **Menu TMS** > **Atualizações** > **Ocorrências** > **Tabela de Ocorrências**, e crie uma ocorrência :

* Do tipo **04 - Retorna Documento**, no programa, conforme exemplo abaixo:

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27149074720535)

* Preencha o campo **DT2\_TIPINS - TIPO DO INSUCESSO** com qualquer tipo de insucesso listado, podendo gerar mais de um tipo de ocorrência, dependendo da necessidade. Os tipos de insucesso definidos pela NT são:

* Recebedor não encontrado;
* Recusa do recebedor;
* Endereço inexistente;
* Outros. Exige Justificativa de no mínimo 25 caracteres antes de envio a **SEFAZ**.

![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27175248850967)

Os campos **DT2\_TIPOCO - TIPO** e **DT2\_TIPINS - TIPO DO INSUCESSO** são essenciais para o procedimento ser efetuado com êxito.

O registro do evento de insucesso e a inclusão de imagem de comprovante de insucesso ocorrerá:

* Ao apontar a ocorrencia de insucesso, o Sistema apresentará a seguinte mensagem. Ao clicar em Sim, você será direcionado para a tela de **TMSAE71B - Manutenção do Comprovante de Entrega**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27606781632279)

* Caso clique em **Não**na mensagem acima, é possível ajustar posteriormente ao selecionar a viagem e clicar em **Outras Ações > Manutenção > Compr Entreg > Altera**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27607668048279)**

Com a tela de **TMSAE71B - Manutenção do Comprovante de Entrega** aberta, clique em **Outras Ações > Seleciona Comprovante de Insucesso**:

![imagem7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27228527430167)

![imagem8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27228924270487)

A inserção da imagem será via *Grid* da rotina, e quando houver um insucesso do tipo Outros, o preenchimento do campo Justificativa será obrigatório.  
Após a inserção dos campos obrigatórios o status passará ao status Apto, conforme imagem:

![imagem9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27228934330391)

**Transmissão**  
Após registrar e complementar o evento de insucesso, deve-se ser transmitido a **SEFAZ**. O processo seguinte é semelhante ao processo de apontamento de comprovante de entrega, na nova tela **TMSAE71A - Monitor de Comprovante de Entrega**. Se estiver na tela de viagem, pode acessá-la em **Outras Ações > Manutenção > Compr Entreg > Monitora.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27607664901271)

Na rotina de Monitor de Transmissão, selecione o documento e acione as operações disponíveis:

* **Transmissão Insucesso**;
* **Cancelar**;
* **Refresh**;
* **Obter** **XML*****.***

***![](https://centraldeatendimento.totvs.com/hc/article_attachments/27606811796631)***

A opção **Transmissão Insucesso** irá transmitir o evento de insucesso para a **SEFAZ**, a opção **Cancelar** irá cancelar a transmissão à **SEFAZ**, o **Refresh** é uma função para atualizar a tela e verificar se foi transmitido o evento e **Obter XML** é para gerar em tela o **XML - Extensible Markup Language** do evento, conforme imagem a seguir:

![imagem10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27228934336023)

**Importante**  
O evento de insucesso poderá ser utilizado apenas para documentos que tenham o *layout* 4.0 do **CT-e - Conhecimento de Transporte Eletrônico**:

![imagem4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27175350956951)

A funcionalidade se aplica tanto na **Viagem modelo 2 -  TMSA144,** como na **Viagem modelo 3 - TMSAF60.**  
  
**Saiba mais**

* [Webinar TOTVS Evento de Insucesso de Entrega de CTe #Totvs\_logistica\_Linha\_protheus](https://www.youtube.com/watch?v=gojdyPcyHXw) traz todo o processo detalhado e simulado em vídeo
* O ajuste da versão dos eventos de comprovante de entrega deve ser feita nos **Eventos** de transmissão. Verifique mais detalhes na documentação [Monitor de Transmissão CTe (TMSAE70 - SIGATMS)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=490964523)
* Documentação da liberação do Evento de Insucesso: [DLOGTMS02-23042 DT Evento de Insucesso Nota Técnica 2023.002 Ajuste SINIEF 50/2022](https://tdn.totvs.com.br/pages/releaseview.action?pageId=821569401)
* Documentação do comprovante de entrega: [Comprovante de Entrega Eletrônico (TMSAE71 - SIGATMS)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=505762262)
* Pacote de Expedição Contínua do **TSS - 12.1.2210:** [24-09-11\_ATUALIZACAO\_12.1.2210\_TSS\_EXPEDICAO\_CONTINUA.ZIP](https://suporte.totvs.com/portal/p/10098/download#detail/1080454)
* Pacote de Expedição Contínua do **TSS - 12.1.2310:** [24-09-11\_ATUALIZACAO\_12.1.2310\_TSS\_EXPEDICAO\_CONTINUA.ZIP](https://suporte.totvs.com/portal/p/10098/download?e=1125788)
* Pacotes de atualização do **TMS - 12.1.2210:** [PACOTE\_DE\_CORRECAO\_000000\_DLOGTMS02-23042\_12.1.2210.ZIP](https://suporte.totvs.com/portal/p/10098/download?e=1134401)
* Pacotes de atualização do **TMS - 12.1.2310:** [PACOTE\_DE\_CORRECAO\_000000\_DLOGTMS02-23042\_12.1.2310.ZIP](https://suporte.totvs.com/portal/p/10098/download?e=1134403)  
    
  **Anexo**
