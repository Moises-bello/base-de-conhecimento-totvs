---
content_hash: 68cf48686fc736b326f71cd5c3c48fd81b1ee0063118340ad05f834a6d566cb1
fetched_at: '2026-06-29T00:10:10.452829+00:00'
page_id: '452719843'
product: rm
source: tdn-rm
title: Provisão de Eventos Adicionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719843
version: 2
---

Nesta etapa será definido como será feito a provisão de eventos adicionais de Férias.  
    
 **Parâmetros**

Provisão de Eventos Adicionais de Férias  
 Conforme a seleção dos parâmetros abaixo, o sistema irá considerar ou não os Eventos Adicionais de férias no Processo de Geração do Histórico de Provisão

* **Sempre Provisionar**: Marcando esta opção, o sistema sempre irá considerar no Processo de Geração do Histórico de Provisão os Eventos adicionais de Férias Globais e os Eventos Adicionais de Férias Individuais.
* **Nunca Provisionar**: Marcando esta opção, o sistema não irá considerar no Processo de Geração do Histórico de Provisões os Eventos Adicionais de Férias Globais e os Eventos Adicionais de Férias Individuais.
* **Provisionar de forma personalizada**: Marcando esta opção será habilitado nos Eventos Adicionais de Férias Globais e nos Eventos Adicionais de Férias Individuais o campo 'Provisionar Eventos'. Com este campo será possível selecionar os eventos que irão ou não compor o cálculo da Geração do Histórico de Provisões.

**Observação**  
 Para cadastrar eventos adicionais de férias Individuais, basta acessar Administração de Pessoal | Cadastros | Funcionários | Anexos | Movimento | Férias, editar um período aquisitivo e em Anexo | Eventos Adicionais, incluir os eventos adicionais.

Proporcionalizar conforme dias de direito  
 Com este parâmetro desmarcado, ao gerar a provisão de férias, o sistema irá somar o valor dos eventos adicionais de férias ao resultado final do cálculo das férias.  
 Com este parâmetro marcado, o sistema irá provisionar os eventos adicionais efetuando a proporcionalização dos mesmos de acordo com os avos de férias adquiridos pelo funcionário.   
 Na geração da provisão será feito um cálculo de proporcionalização em cima dos valores de adicionais de férias.

**Exemplo**  
 O evento adicional de férias retornou o valor de R$ 1.000,00  
 O funcionário possui 10 avos de férias  
 Com o parâmetro marcado o sistema irá fazer o seguinte cálculo:  
 (1.000,00 / 12) \* 10 = 833,33  
    
 Lembrando que, com a opção "Provisionar de forma personalizada" marcada, o sistema irá proporcionalizar os eventos que tiverem a opção "Provisionar eventos" marcada.   
    
 **Atenção**  
 É importante ressaltar que este parâmetro somente ficará habilitado quando a opção "Nunca Provisionar" estiver desmarcada.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<< Retornar para **Férias**
