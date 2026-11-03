---
article_id: 36606435494423
category: GPE - eSocial - Não Periódicos
content_hash: bfdca39af5e53413bcca7d80ab5b3ac990ad7bc9cd3ded182613379b7dcb656c
fetched_at: '2026-06-28T22:45:04.653647+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2205 - Como informar dados de deficiência
  no evento S-2205
type: support-article
updated_at: '2026-06-16T13:47:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36606435494423-RH-Linha-Protheus-GPE-eSocial-S-2205-Como-informar-dados-de-defici%C3%AAncia-no-evento-S-2205
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36606435482007) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como gerar informações de deficiente no evento S-2205?  
  
**Ambiente**  
TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para que o sistema leve as informações nas tags de deficiencia do S-2205 ([infoDeficiencia](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-s-1-3-cons-ate-nt-04-2025-rev-26-08-2025/index.html/#r_2205_alteracao_dadosTrabalhador_infoDeficiencia)) é necessário alterar o cadastro do funcionário conforme abaixo:  
  
- Acesse o caminho GPE - Atualizações - Funcionários - Funcionários. Após selecionar o funcionário clique em Alterar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36607246013591)  
  
**- Defic.Fisico (RA\_DEFIFIS)**: **1** se o funcionário for Deficiente Fisico / **2** se o funcionario não for deficiente físico  
**- BR/DH (RA\_BRPDH):**  Informe se o funcionario é Beneficiario Reabilitado, Portador de deficiencia Habilitado ou se não se aplica. Campo utilizado para geração do Perfil Profissiográfico Previdenciário e para gerar a tag reabReadap  
**-** **Tp. Deficien (RA\_TPDEFFI):** Informe o tipo de deficiência física do funcionário.   
**- Defi. eSocial (RA\_PORTDEF):** Informar se o trabalhador enquadra-se em uma ou mais situações disponíveis, quanto a sua deficiência se possuir. Uso eSocial. Será **permitida múltipla escolha**, com as seguintes opções:  
Física / Auditiva / Visual / Mental / Intelectual / Reabilitado.  
**- Cota Def (RA\_CTPCD):** Informe neste campo se o funcionário preenche a cota de pessoas com deficiência. Gerando a tag infoCota para o eSocial.  
  
**Atenção**: caso o parametro MV\_OPESOC esteja habilitado, o sistema **não gera o S-2205** com informações de deficiência pois entende que se trata de Entes Públicos e a informação de deficiência não existe no leiaute dos eventos S-2400 e S-2405.  
O parametro por **padrão é .F.** no dicionário de dados, somente altere caso se trate de Entes Públicos.  
  
O evento S-2205 será gerado de acordo com a **data base do Sistema**:  
[RH - Linha Protheus - GPE - eSocial - S-2205 - Como gerar um evento S-2205 (Alteração de Dados Cadastrais do Trabalhador) com data retroativa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23127814682391-RH-Linha-Protheus-GPE-eSocial-S-2205-Como-gerar-um-evento-S-2205-Altera%C3%A7%C3%A3o-de-Dados-Cadastrais-do-Trabalhador-com-data-retroativa)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
