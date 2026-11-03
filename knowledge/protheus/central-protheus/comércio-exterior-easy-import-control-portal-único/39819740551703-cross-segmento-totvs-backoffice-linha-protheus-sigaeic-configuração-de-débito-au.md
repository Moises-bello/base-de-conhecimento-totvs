---
article_id: 39819740551703
category: Comércio Exterior - Easy Import Control - Portal Único
content_hash: d66b93bbf54b69c3280fc2501e8b1b4469c55517daaa8ff8bdef56d40af7e618
fetched_at: '2026-06-28T22:39:40.280395+00:00'
product: protheus
section_id: 27387892471703
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) -  SIGAEIC  - Configuração
  de Débito Automático de Impostos na DUIMP
type: support-article
updated_at: '2026-04-23T13:27:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39819740551703-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Configura%C3%A7%C3%A3o-de-D%C3%A9bito-Autom%C3%A1tico-de-Impostos-na-DUIMP
---

O pagamento automático dos tributos federais no registro da DUIMP pelo Protheus é feito via PCCE, após autorização bancária no Internet Banking e configuração no Portal Único Siscomex com certificado digital. O débito automático para ICMS depende da integração estadual; caso contrário, geram-se guias. Em falhas, contate o suporte SERPRO.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39819740540311) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como configurar o débito automático dos impostos federais para o registro da DUIMP (Declaração Única de Importação) pelo Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control (SIGAEIC) - A partir da versão 12.1.33  
  
**Solução**

O pagamento dos tributos federais (II, IPI, PIS, COFINS) e demais taxas no registro da DUIMP é realizado através do **PCCE (Pagamento Centralizado do Comércio Exterior)**. Para que o débito ocorra automaticamente no momento da transmissão/registro pelo Protheus, a configuração deve ser efetuada diretamente no Portal Único Siscomex, após autorização bancária.

##### **Passos**

**1. Autorização Bancária Prévia**

1. Acesse o Internet Banking da instituição financeira onde a empresa possui conta;
2. Realize a autorização para **Débito Automático de Pagamentos Siscomex/Receita Federal**;

   * *Nota:* Sem esta etapa prévia junto ao gerente ou sistema do banco, a transação enviada pelo portal será rejeitada.

**2. Configuração no Portal Único Siscomex (PCCE)**

1. Acesse o **Portal Único Siscomex** utilizando o Certificado Digital da empresa;
2. No menu de módulos, selecione **Pagamento Centralizado (PCCE)**;
3. Navegue até **Manter Conta Bancária** ou **Gestão de Contas**;
4. Clique em **Incluir** e informe os dados da conta (Banco, Agência e Conta Corrente) que foi autorizada no passo anterior;
5. Salve as alterações para que a conta fique disponível para o sistema.

**3. Registro da DUIMP no Protheus**

1. No módulo **SIGAEIC**, ao finalizar o preenchimento dos dados da DUIMP e prosseguir para a etapa de registro;
2. O sistema enviará as informações ao Portal Único, que por sua vez utilizará a conta cadastrada no PCCE para efetivar o débito dos tributos federais;
3. Para o **ICMS** (Estadual), o fluxo também ocorre via PCCE, porém a disponibilidade do débito automático depende da integração da SEFAZ de cada estado. Caso não haja integração, será necessária a geração de guias (GNRE/DAE).

Em caso de falhas na comunicação com a conta bancária dentro do portal, o contato deve ser feito diretamente com o suporte da SERPRO.

**Saiba mais:**  
[**EIC 001 - FAQ - Novo processo de Importação - Portal Único**](https://tdn.totvs.com/pages/releaseview.action?pageId=788602791)
