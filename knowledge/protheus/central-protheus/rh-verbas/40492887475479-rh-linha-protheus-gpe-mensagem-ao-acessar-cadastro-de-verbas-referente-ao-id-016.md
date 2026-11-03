---
article_id: 40492887475479
category: 'RH - Verbas '
content_hash: 5b02a0fadfe44880da3fbcf9c30a5674894dc3952856aaed5db2764879d49224
fetched_at: '2026-06-28T22:43:19.855875+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: 'RH - Linha Protheus - GPE -  Mensagem ao acessar cadastro de verbas referente
  ao id 0168: Verificada inconsistência para verba de Id 0168 - Dedução INSS Base
  IR Férias, cadastrada como 3-Base (Provento).'
type: support-article
updated_at: '2026-05-15T12:43:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40492887475479-RH-Linha-Protheus-GPE-Mensagem-ao-acessar-cadastro-de-verbas-referente-ao-id-0168-Verificada-inconsist%C3%AAncia-para-verba-de-Id-0168-Dedu%C3%A7%C3%A3o-INSS-Base-IR-F%C3%A9rias-cadastrada-como-3-Base-Provento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40492860998807) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao acessar o cadastro de verbas é gerado a mensagem:  
Verificada inconsistência para verba de Id 0168 - Dedução INSS Base IR Férias, cadastrada como 3-Base (Provento).   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Em ambientes migrados da versão 11 para a 12, a verba informativa com Id 0168 era do tipo 3-Base (Provento). No entanto, conforme a Tabela 54 do eSocial, a rubrica de Previdência Social sobre Férias deve ser informada como base Desconto (4 - informativa dedutora).  
O campo Tp.Cod. é **bloqueado para edição** na alteração do Cadastro de Verbas. Dessa forma, ao conferir os valores na substituição da DIRF, o eSocial demostra o valor como negativo no totalizador do portal. Além disso, há soma quando existe a verba de Id 1723 utilizada para realizar a contrapartida da dedução de INSS aplicada na base de IRRF de férias.

Ao acessar a rotina do Cadastro de Verbas com eSocial ativo, serão verificados os registros da tabela SRV e, caso exista verba com Id 0168-Dedução INSS Base IR Férias cadastrada com o tipo 3, será alertado em tela, possibilitando ao usuário executar o ajuste quando lhe for conveniente:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40492887457559)

-Ao selecionar **Não**, segue normalmente para o browse do cadastro, informando novamente num novo acesso.

-Selecionando **Sim**, o ajuste de base é executado, atualizando o Tipo do Código de 3 para 4, e efetuando a integração da rubrica ao eSocial.   
Ao final é exibido um log do processamento das integrações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40492887458711)

-Verba de id 0168 alterada de 3-Base (Provento) para 4-Base (Desconto).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40492889439127)

**Saiba Mais**  
[Documentação Técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=1062388104)
