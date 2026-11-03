---
article_id: 360024378171
category: Gestão de Transportes (TMS)
content_hash: e8cdb8215a7d9f2fe05a466cc7f3b853b785badb8642440f0242c6bc07d32a0b
fetched_at: '2026-06-28T22:45:27.474297+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como gravar a Natureza - E1_NATUREZ nos
  títulos a receber gerados pelo módulo SIGATMS
type: support-article
updated_at: '2025-07-29T13:57:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024378171-Log%C3%ADstica-Linha-Protheus-TMS-Como-gravar-a-Natureza-E1-NATUREZ-nos-t%C3%ADtulos-a-receber-gerados-pelo-m%C3%B3dulo-SIGATMS
---

![rel_gio_kcs.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041496193) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como gravar a **Natureza -**  **E1\_NATUREZ** nos títulos a receber gerados pelo módulo **SIGATMS - Gestão de Transportes**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
 **Solução**

A gravação da **Natureza - E1\_NATUREZ** nos títulos a receber gerados pelo módulo **SIGATMS** é obtida dos campos **Natureza - DC5\_NATURE** e **Natureza - A1\_NATUREZ**, dependendo de como estiver configurado o parâmetro **MV\_TMSMFAT**:  
  
- Se o **MV\_TMSMFAT** for igual a **1:****1º** - **Natureza -** **DC5\_NATURE** -  Em **Atualizações/Cadastros/Serviços x Tarefas - DLGA070.** Utilizamos um registro com **Categoria de Serviço de Negociação**, onde, este serviço deve estar associado ao contrato do cliente e nele, informamos o código de natureza conforme o exemplo utilizado abaixo, **DC5NAT**. O preenchimento deste campo não é obrigatório, mas, uma vez preenchido, ao calcular qualquer operação de frete, o sistema utilizara automaticamente este código de natureza, desconsiderando o parâmetro **MV\_1DUPNAT.**

![image__7_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405501369239)

**2º -** **Natureza -** **A1\_NATUREZ -** Se o campo **Natureza -** **DC5\_NATURE** estiver vazio**,**será considerada a Natureza informada no cadastro de cliente devedor **Natureza - A1\_NATUREZ**.  
  
- Se **MV\_TMSMFAT** for igual a **2**, serão consideradas as seguintes opções:

* Quando utilizar a rotina **Fatura Automática -TMSA491** irá gravar a natureza informada no parâmetro **MV\_NATFAT** **- Código da Natureza** do título de transporte;
* Quando utilizar a rotina **Fatura por Documento -TMSA850**, será gravado a natureza informada no filtro da rotina, por meio de **Atualizações/Financeiro/Fatura por Docto,** clique em **Selecionar**, será apresentada a tela de **Faturas a Receber** onde temos o campo **Natureza**.

![image__8_.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405501634711)

**Em ambos os casos citados, o registro no Financeiro será gerado apenas após a execução das rotinas citadas.**Além do parâmetro **MV\_TMSMFAT**, deve-se verificar o conteúdo parâmetro **MV\_1DUPNAT** **- Campo ou dado a ser gravado na natureza do titulo** do **Financeiro para documentos de saída**. O Sistema busca o parâmetro **MV\_1DUPNAT** para verificar onde buscar a **Natureza**, o valor padrão é **SA1->A1\_NATUREZ**. A alteração deste parâmetro pode ter impacto na geração dos títulos a pagar de **ISS - Imposto sobre Serviço**.
