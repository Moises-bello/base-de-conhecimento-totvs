---
content_hash: 56371dd7871b38bc3527c903f7da5424b25ca2d9863e8f45482caf569eed437d
fetched_at: '2026-06-29T00:09:14.955467+00:00'
page_id: '421385316'
product: rm
source: tdn-rm
title: Custo Horário  
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385316
version: 3
---

---

Serão listados os recursos que poderão ser utilizados na formula.  
 Recursos com iniciais "I" representam insumos, "C" representam composições auxiliares.  
 Variáveis que poderão ser aplicadas para o Custo Produtivo ou Custo Improdutivo

* QT- Quantidade
* VL- Valor
* VU- Valor unitário
* EQ- Equipe
* VI- Valor improdutivo
* DP- DMT (Pav)
* DT- DMT (Terra)
* DR-DMT (Revestido)

**Observações:**  
 Se a composição for do tipo Equipamento, o custo produtivo e improdutivo dever estar habilitada e deverá existir ao menos um recurso do tipo equipamento.  
 Se a composição for do tipo Mão de Obra, somente o custo produtivo dever estar habilitado e deverá existir ao menos um recurso do tipo mão de obra.  
 Os recursos que fazem parte da fórmula não poderão ser excluídos, tanto na tela de edição de composição quanto na tela de visão de recursos.  
 A fórmula só será utilizada no calculo, caso a composição se torne auxiliar de outra.  
  
**Exemplo:**  
 Composição X – "Descrição da composição X", que possui os recursos:  
 Insumo: 01 - Caminhão  
 Insumo: 02 - Servente  
 Composição Y –"Descrição da composição Y"  
  
 Fórmulas:  
 Valor Produtivo: I1.QT + I2.VL + C3.VU   
 Valor Improdutivo: I1.QT + I2.VL + C3.VU^2  
 Onde I1, I2 e C3 são os identificadores dos recursos da composição, sendo "I" para insumos e "C" para composições auxiliares.  
 Na formula poderá ser aplicado, Operadores: +, -, \*, /, ^ e MOD e Funções: Trunc, Round, Abs, ArcTan, Cos, Exp, Frac, Int, Log, Pi, Sin, Sqr, Sqrt.  
  
**Exemplo:**  
 Valor Produtivo: Trunc(C1.VL)  
 As composições do tipo equipamento podem ser utilizadas no cálculo da composição por produção.  
 Se marcado Composição por produção, no campo chefe de equipe ou aba Produção da Equipe Mecânica poderá ser informada uma composição do tipo equipamento como chefe da equipe.  
 Se seu produto estiver com a Biblioteca na versão 11.20.15 ou posterior, veja o novo cálculo do custo horário acessando .
