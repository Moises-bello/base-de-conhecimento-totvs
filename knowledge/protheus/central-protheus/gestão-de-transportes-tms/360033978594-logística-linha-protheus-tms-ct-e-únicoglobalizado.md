---
article_id: 360033978594
category: Gestão de Transportes (TMS)
content_hash: e1e87e6fbae956f9f644918f4865a77faf0020d8581ab806eadec32ad326abcd
fetched_at: '2026-06-28T22:45:27.630326+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - CT-e Único/Globalizado
type: support-article
updated_at: '2026-05-05T20:26:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033978594-Log%C3%ADstica-Linha-Protheus-TMS-CT-e-%C3%9Anico-Globalizado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22902789139479)** Tempo aproximado para leitura: **00:02:10 min**  
  
**Dúvida**  
Quais os procedimentos para geração do **CT-e** **Único**/**Globalizado?**  
  
**Ambiente**

TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
O **CTe Único**, ou **CTe Globalizado**, é um documento que abrange diversas operações de transporte, as quais anteriormente seria necessário emitir vários documentos. Esse processo permite que todas as operações sejam atendidas por um único **CTe**.   
  
Esta modalidade pode ser utilizada, considerando:

* O tomador deve ser o remetente ou o destinatário das mercadorias transportadas.
* A operação de transporte deve abranger no mínimo cinco remetentes ou cinco destinatários.
* As mercadorias transportadas estejam acobertadas com **Notas Fiscais Eletrônicas**.
* O campo **Tipo do CT-e,** no **TMS** é o campo **DTC\_TIPNFC - Tipo Nf Cli**, será preenchido com **0** **- CT-e Normal**.

No TMS, para incluir um **CTe** Único, é necessário:

* Acessar a rotina **TMSA050 - Entrada de documentos;**
* No campo de **DTC\_LOTNFC** **- No.Lote,** clique na lupa ou na tecla **F3** e inclua um lote com o campo **DTP\_QTDLOT - Qtd.Lote** igual ou maior que **5**e o campo **DTP\_TIPLOT - Tipo Lote**igual a  **4 - CTe Unico(Globalizado);**
* Com o lote de **CTe Único** cadastrado, inclua uma entrada de documento para cada conjunto de remetente e destinatário. Por exemplo, em um cenário que há um remetente e 5 destinatários, será necessário incluir uma entrada de documentos para cara combinação de remetente e destinatário, utilizando o mesmo lote, conforme exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22922607647255)

* Após concluir a digitação dos documentos, calcule o documento e valide se o Sistema gerou uma única numeração de **CTe**;
* Com o **CTe** gerado, transmita-o para a **SEFAZ**.

Vale destacar que é necessário respeitar as validações definidas pela **SEFAZ** no **Manual do Contribuinte do CTe**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22907968899095)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22907968910871)

**Importante**  
O **CTe Globalizado** pode ser emitido para clientes dos estados **SC, PR, MS, BA e GO** ou clientes de outros estados que possuam **regime especial** para este tipo de emissão. No caso de regime especial, é necessário utilizar o ponto de entrada [TM200UFUNI - Acrescenta UF para a geração do CTe Globalizado](https://tdn.totvs.com/pages/releaseview.action?pageId=847881612).  
Nos estados de SP e MG, o **CTe Globalizado** foi descontinuado a partir de abril de 2026, caso ele seja transmitido, a **SEFAZ** rejeitará. O **CTe Globalizado** foi substituído pelo **CTe Simplificado.**  
  
**Glossário**  
**CT-e** - Conhecimento de Transporte eletrônico  
**SEFAZ** - Secretaria da Fazenda  
**TMS** - Transportation Management System  
  
**Anexo**  
[CTe Simplificado (TMSA493 - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=936464344)  
[CTe Simplificado - Configuração (TMSA493 - SIGATMS)](https://tdn.totvs.com/pages/viewpage.action?pageId=940305448)  
Segue em anexo boletim técnico e vídeo com exemplo de uso do **CT-e Único** no Sistema.
