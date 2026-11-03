---
article_id: 1500006232721
category: GPE - eSocial - Não Periódicos
content_hash: 278365a1741f2d5d44ec9589502ab76da3ef4211804c6a3e102bf661e031d517
fetched_at: '2026-06-28T22:45:04.719880+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - O sistema não gera o evento
  S-2206 quando é feito uma transferência de centro de custo
type: support-article
updated_at: '2026-06-16T10:52:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006232721-RH-Linha-Protheus-GPE-eSocial-S-2206-O-sistema-n%C3%A3o-gera-o-evento-S-2206-quando-%C3%A9-feito-uma-transfer%C3%AAncia-de-centro-de-custo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19463267927703)**Tempo aproximado para leitura: 00:**02:00 min  
  
Ocorrência**O sistema não gera o **evento S-2206** quando é feito uma **transferência** de centro de custo no SIGAGPE  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**No eSocial centro de custo (**evento S-1020 Lotação Tributaria**) não está vinculado diretamente ao trabalhador no evento **S-2200,** por isso não vai existir a geração do **S-2206**.  
  
**Solução**Esse comportamento do sistema está correto. A transferência de centro de custo (**evento S-1020 Lotação Tributaria**) não gera alteração contratual (**S-2206**) no **eSocial**, essa geração ocorre apenas quando o centro de custo é uma Obra Total. No casos de Obra Total o sistema está configurado com o Tipo de Lotação 01 e CNO, nesse cenário esse centro de custo além de ser uma **Lotação Tributaria** (evento S-1020) é um **Estabelecimento** (evento S-1005).  
  
Para o **eSocial** a transferência ocorre quando ela for de Estabelecimento (S-1005), ou seja, somente se for uma Filial ou um Centro de Custo que esteja configurado para ser Obra Total, ou seja, caso a transferência seja realizada entre estabelecimentos com a mesma raiz de CNPJ o evento a ser gerado é o S-2206. Em caso de transferência entre raiz de CNPJ diferentes, será gerado o evento S-2200 para a empresa de destino e S-2299 para empresa origem.  
  
O governo sabe em qual centro de custo (lotação tributaria) o trabalhador está no momento em que é gerado o S-1200, pois todas as verbas da folha vão para o eSocial vinculadas ao centro de custo (lotação) e estabelecimento que ele está alocado.  
  
**Observação**  
Para entender mais sobre cadastros de Obras no eSocial consulte os artigo:

* [MP - GPE- eSocial - Obras - S-1005 x S-1020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030600113)
* [MP - GPE- eSocial - S-2200 - Como vincular o cadastro de funcionário a um CNO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003515442)

**Saiba Mais**Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
**Próximos Treinamentos**  
*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
