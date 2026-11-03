---
article_id: 14191172101655
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: c7f6161b639ae2ee7187a25b7b42568c1446849f536b41ba7acd8fd3c1d2787d
fetched_at: '2026-06-28T22:37:56.250011+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA430 - Retorno de
  pagamento DDA que possui títulos de outras filiais
type: support-article
updated_at: '2025-09-30T16:40:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14191172101655-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA430-Retorno-de-pagamento-DDA-que-possui-t%C3%ADtulos-de-outras-filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35303480702103) Tempo aproximado para leitura: **00:15:00 min** **Dúvida**Ao recepcionar o arquivo de retorno do banco DDA pela rotina "**FINA430** - Retorno de pagamento" que possui títulos de outras filiais, o sistema está gravando a filial logada (FIG\_FILIAL) para todos os títulos, ao invés de gravar a filial (FIG\_FILIAL) correspondente de cada título, como corrigir?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**Caso o banco não tenha a flexibilidade de enviar em arquivos de **retorno DDA separado por filiais**, poderá utilizar o ponto de entrada abaixo:  
["F430GRAFIL - Gravação da filial de origem na tabela FIG - Conciliação DDA"](https://tdn.totvs.com/pages/releaseview.action?pageId=648838725)  
  
Mas para o funcionamento correto do ponto é necessário que tenha algumas configurações no seu **layout de retorno de pagamento DDA**.  
  
Segue os pontos:  
**1)** É necessário que o seu banco envie no **arquivo** **de retorno do banco DDA**, o **CNPJ** de cada filial com os títulos correspondentes.  
  
**Exemplo:**  
Veja que na posição 1 (círculo em vermelho) que é a posição do ["*Header"*](https://tdn.totvs.com/pages/releaseview.action?pageId=243639259) possui o CNPJ da filial 01 (retângulo em vermelho)

[![1_-_arquivo_de_retorno.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/14326211059607)](https://centraldeatendimento.totvs.com/hc/article_attachments/14326211059607)  
  
**2)** No seu **sigamat** esteja cadastrado o **CNPJ de cada filial** que vem dentro do **arquivo de retorno do banco DDA.**  
  
**Exemplo:**  
Acessar a rotina **SIGACFG > Ambiente > Empresas > Filial**, e confirme se o **CNPJ** está cadastrado para cada filial correspondente

![2_filial_no_sigamat.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/14191298900247)

**3)** Editar o seu **layout a pagar de retorno CNAB DDA**, na opção:  
**SIGACFG > Cadastros > CNAB Modelo 2**  
  
E no *Header* do seu **layout**, coloque a posição inicial e final referente ao **CNPJ da sua empresa** seguindo a documentação em PDF do banco que possui contrato.  
Utilize a variável **CGCEMP** no conteúdo da posição CNPJ.  
  
**CGCEMP** - Para **layout DDA**, utilize essa variável na posição "*Header*" para posicionar em cada **CNPJ de cada filial**, para o funcionamento do ponto de entrada **F430GRAFIL**

![3_header_layout.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/14191712085527)

**4)** Compile o [exemplo do ponto de entrada **F430GRAFIL**](https://tdn.totvs.com/pages/releaseview.action?pageId=648838725) e já poderá utilizar.  
[Faça download do layout a pagar DDA utilizado no exemplo](https://centraldeatendimento.totvs.com/hc/article_attachments/14202246554263)

**Sabia mais**[Conciliação DDA (FINA260 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312165346)  
[F430GRAFIL - Gravação da filial de origem na tabela FIG - Conciliação DDA](https://tdn.totvs.com/pages/releaseview.action?pageId=648838725)  
[FIN0026\_CNAB\_Registro\_de\_linha\_retorno\_Modelo\_2](https://tdn.totvs.com/pages/releaseview.action?pageId=243639259)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Configuração Multicontas Correntes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021667552-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Configura%C3%A7%C3%A3o-Multicontas-Correntes)  
[Webinar | MP SIGAFIN Desvendando o CNAB #TOTVS\_Backoffice\_Linha\_Protheus](https://www.youtube.com/watch?v=zExMphjmRtI&t=1524s)
