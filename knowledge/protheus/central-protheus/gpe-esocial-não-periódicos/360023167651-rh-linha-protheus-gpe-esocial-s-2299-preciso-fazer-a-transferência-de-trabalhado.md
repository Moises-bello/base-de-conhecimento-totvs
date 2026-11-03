---
article_id: 360023167651
category: GPE - eSocial - Não Periódicos
content_hash: 70e65f4a33764ecfbc0cb34a9d36b8d8b7a0b9be9e425f482764610cff426125
fetched_at: '2026-06-28T22:45:05.880608+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - Preciso fazer a Transferência
  de trabalhadores do Protheus para uma empresa que não utiliza o Protheus, como fazer
  isso no sistema
type: support-article
updated_at: '2026-06-18T17:40:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023167651-RH-Linha-Protheus-GPE-eSocial-S-2299-Preciso-fazer-a-Transfer%C3%AAncia-de-trabalhadores-do-Protheus-para-uma-empresa-que-n%C3%A3o-utiliza-o-Protheus-como-fazer-isso-no-sistema
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25103530664983)Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**  
Preciso fazer a **Transferência** de trabalhadores do Protheus para uma empresa que não utiliza o Protheus, como fazer isso no sistema.  
  
Exemplo:  
A empresa **A** que **NÃO** utiliza Protheus incorporou a empresa **B** que utiliza Protheus, com os empregados da empresa **B** sendo então transferidos para empresa **A**.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
Foi implementado uma opção na rotina de transferências onde é permitido realizar “**Transferência Externa**”. Para que esta opção seja demonstrada na rotina de Transferência - **atualizações >funcionários >transferência > outras ações**, o parâmetro MV\_RHTAF precisa estar habilitado = .T.:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25103520066839)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25103520070679)  
Ao parametrizar com o CNPJ da empresa destino, tipo de rescisão e data de desligamento, o sistema irá gerar o evento S-2299(Desligamento) com sucessão de vínculo para o CNPJ informado, o motivo de desligamento e os campos da SRA serão atualizados de acordo com o tipo de rescisão selecionado.  
  
**Como fazer a transferência externa:**  
  
1. No SIGAGPE acesse o caminho **atualizações > funcionários > transferências;**

2. Selecione a opção **Transferência Externa** no botão **Outras Ações;**

2. Preencha os parâmetros de acordo com a descrição.

2.1 O campo tipo de rescisão deve ser vinculado a um tipo de rescisão da tabelas **S043** que tenha a coluna **motivo eSocial** relacionado a transferência. Também é importante observar as colunas Cod. Resc. Rais e Cod. Afast FGTS, pois os campos do cadastro do funcionário **RA\_RESCRAI** e **RA\_AFASFGT** serão preenchidos de acordo com essa opção.  
Caminho S043*:* **atualizações > definição de cálculos > manutenção de tabelas**  
  
**Print de exemplo Transferência Externa. Observação: As informações devem ser preenchidas de acordo com a situação da empresa. Caso tenha dúvidas no preenchimento dos campos, orientamos verificar com o Jurídico da Empresa.**  
  
*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10015513274263)*  
*![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10015516623511)*

Caso a opção não habilite no menu Transferencias, por favor valide se os parametros do link abaixo estão corretos:  
https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004980892-RH-Linha-Protheus-GPE-eSocial-Par%C3%A2metros-2%C2%AA-Fase-esocial-N%C3%A3o-Peri%C3%B3dicos

**Saiba Mais**  
Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
[Chatbot com as principais dúvidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991/)
