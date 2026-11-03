---
article_id: 360052055574
category: Integrações Nativas
content_hash: c5e1a472594072d91211da9e13657cab985f0e2531c2c1c3d3b9f175ed0c6803
fetched_at: '2026-06-28T22:42:35.354319+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Baixa de títulos do tipo Multa - Manutenção
  de Ativos integrado com o Financeiro
type: support-article
updated_at: '2025-01-23T13:04:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052055574-Manufatura-Linha-Protheus-MNT-Baixa-de-t%C3%ADtulos-do-tipo-Multa-Manuten%C3%A7%C3%A3o-de-Ativos-integrado-com-o-Financeiro
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:45 min** **Dúvida**Como é realizada a baixa de títulos a pagar do tipo **Multa** quando **Manutenção de Ativos - SIGAMNT** está integrado ao **Financeiro - SIGAFIN**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Solução**Primeiramente para utilização do **Manutenção de Ativos** integrado ao **Financeiro** deve ser realizada a configuração abaixo:  
  
 No **Configurador - SIGACFG** acesse **Ambientes/Cadastros/Parâmetros - CFGX017**. Configure o parâmetro **MV\_NGMNTFI**

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| **Nome** | **MV\_NGMNTFI** |
| **Tipo** | *Caracter* |
| **Cont. Por.** | **S** |
| **Descrição** | **Integração Manutenção (MNT) com Financeiro (FIN)****Informar S=Sim ou N=Não.** |

**Cadastros Prévios**  
1. Em **Infrações Trans. - MNTA770**deve ser incluída uma infração de trânsito;  
2. Em **Veículos** - **MNTA084**, incluir um **Veículos**, com o campo **Categoria** igual a **4 – Frota não Integrado ao TMS -Transportation Management Systems** e informe o estado no campo **UF Emplac. - T9\_UFEMPLA.**Segue abaixo os procedimentos para baixa de títulos utilizando o **Manutenção de Ativos** integrado ao **Financeiro**:  
  
1. No módulo **Manutenção de Ativos - SIGAMNT** acesse **Atualizações/Controle de Riscos/Multas/Org. Autuadores - MNTA775**. Selecione a opção **Incluir**, informe os dados conforme *help* de campo e confirme.  
2. Acesse **Atualizações/Controle de Riscos/Multas/Notificações - MNTA766**. Selecione a opção **Incluir**, informe os dados conforme *help* de campo e confirme.  
3. Posicione o *cursor* na notificação e selecione a opção **Outras ações - Gerar multa**. Informe os dados conforme *help* de campo e confirme.  
4. Para consultar a multa, acesse **Atualizações/Controle de Riscos/Multas/Multas - MNTA765**.  
5. Acesse **Atualizações/Gestão de Documentos/Cadastros/Documentos - MNTA705**. Selecione a opção **Incluir**, informe os dados conforme *help* de campo e confirme.  
6. Acesse **Atualizações/Gestão de Documentos/Cadastros/Dcto Obrigat. Veículo - MNTA805**. Posicione o *cursor* em um Bem e clique em **Documento**. Selecione a opção **Incluir**, informe os dados conforme *help* de campo e confirme.  
7. Acesse **Atualizações/Gestão de Documentos/Cadastros/Servico/Despachante - MNTA980**. Selecione a opção **Incluir** e relacione o(s) documento(s) **Item 8** ao **Serviço**. Informe os dados conforme *help* de campo e confirme. Neste item é possível estabelecer em que momento serão gerados os honorários ao despachante, por meio do campo **Pag. Honor. - TS4\_PAGHON.**8. Acesse as opções **Atualizações/Gestão de Documentos/Cadastros/Serviço/Fornecedor - MNTA950**. Selecione a opção **Incluir**, e relacione o(s) serviço(s) **Item 13** ao **Fornecedor**. Informe os dados conforme *help* de campo e confirme. Neste item é possível estabelecer qual é o**Custo do Serviço**.  
9. No módulo **Financeiro - SIGAFIN** acesse as opções **Atualizações/Contas a Pagar/Baixas Pagar Man. - FINA080**. Posicione o cursor em um **Título** e selecione a opção **Baixar**. Informe os dados conforme *help* de campo e confirme. Nesse momento, o Sistema realiza a baixa da **Multa** e do documento gerado.  
10. No módulo **Manutenção de Ativos - SIGAMNT** acesse as opções **Atualizações/Controle de Riscos/Multas/Multas - MNTA765**. Posicione o cursor na **Multa** paga e selecione a opção **Visualizar**. Acesse a pasta **Pagamento**, para visualizar que a multa foi paga e, caso haja desconto, também foi atualizado.  
11. Acesse **Atualizações/Gestão de Documentos/Custos/Honorários Despach. - MNTA666**. Informe os dados conforme *help* de campo e confirme.  Será apresentada a tela de todos os serviços prestados pelo **Fornecedor**. Marque o(s) serviço(s) e **confirme**.  
12. No **Financeiro - SIGAFIN** acesse as opções **Atualizações/Contas a Pagar/Baixas Pagar Man. -FINA080**. Posicione o cursor em um **Título** e selecione a opção **Baixar**. Informe os dados conforme *help* de campo e confirme. O Sistema irá baixar o **Honorário do Despachante** gerado.
